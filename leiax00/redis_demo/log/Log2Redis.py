# coding: utf-8
import bisect
import logging
import time
from datetime import datetime

import redis

from redis_demo.redis_client import conn

SEVERITY = {
    logging.DEBUG: 'debug',
    logging.INFO: 'info',
    logging.WARNING: 'warning',
    logging.ERROR: 'error',
    logging.CRITICAL: 'critical'
}
# 把字典dict2的键/值对更新到dict里。
SEVERITY.update((name, name) for name in SEVERITY.copy().values())


def log_recent(conn, name, message, severity=logging.INFO, pipe=None):
    severity = str(SEVERITY.get(severity, severity)).lower()
    destination = 'recent:%s:%s' % (name, severity)
    message = time.asctime() + '  ' + message
    pipe = pipe or conn.pipeline()
    pipe.lpush(destination, message)
    pipe.ltrim(destination, 0, 5)  # 裁剪日志列表，只包含最新的6条信息
    pipe.execute()


def log_common(conn, name, message, severity=logging.INFO, timeout=5):
    """
    一小时内消息的频率数
    """
    severity = str(SEVERITY.get(severity, severity)).lower()
    destination = 'common:%s:%s' % (name, severity)
    start_key = destination + ':start'
    pipe = conn.pipeline()
    end = time.time() + timeout
    while time.time() < end:
        try:
            pipe.watch(start_key)
            # time.struct_time(tm_year=2019, tm_mon=2, tm_mday=18, tm_hour=15, tm_min=32, tm_sec=10, tm_wday=0,
            # tm_yday=49, tm_isdst=-1)
            now = datetime.utcnow().timetuple()
            hour_start = datetime(*now[:4]).isoformat()
            hour_start = datetime.fromisoformat(hour_start).timestamp()

            existing = pipe.get(start_key)
            pipe.multi()
            # 每小时更新一个key
            if existing is None:
                pipe.set(start_key, hour_start)
            elif float(existing) < hour_start:
                pipe.rename(destination, destination + ':last')
                pipe.rename(start_key, destination + ':pstart')
                pipe.set(start_key, hour_start)

            pipe.zincrby(destination, 1, message)
            log_recent(pipe, name, message, severity, pipe)
            return
        except redis.exceptions.WatchError:
            print('start_key has changed....')
            continue


SAMPLE_COUNT = 1


def clean_counters(conn):
    pipe = conn.pipeline(True)
    passes = 0
    while True:
        start = time.time()
        index = 0
        while index < conn.zcard('know:'):
            hash = conn.zrange('known:', index, index)
            index += 1
            if not hash:
                break
            hash = hash[0]
            prec = int(hash.partition(':')[0])
            bprec = int(prec // 60) or 1
            if passes % bprec:
                continue
            hkey = 'count:' + hash
            cutoff = time.time() - SAMPLE_COUNT * prec
            samples: list = map(int, conn.hkeys(hkey))
            samples.sort()
            remove = bisect.bisect_right(samples, cutoff)
            if remove:
                conn.hdel(hkey, *samples[:remove])
                if remove == len(samples):
                    try:
                        pipe.watch(hkey)
                        if not pipe.hlen(hkey):
                            pipe.multi()
                            pipe.zrem('known:', hash)
                            pipe.execute()
                            index -= 1
                        else:
                            pipe.unwatch()
                    except redis.exceptions.WatchError:
                        pass
        passes += 1
        duration = min(int(time.time() - start) + 1, 60)
        time.sleep(max(60 - duration, 1))


if __name__ == '__main__':
    # log_recent(redis_conn, 'name', 'message')
    log_common(conn, 'name', 'message')
