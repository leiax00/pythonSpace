# coding: utf-8
import logging
import time
from datetime import datetime

import redis

from redis_demo.RedisClient import redis_conn

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
            if existing and float(existing) < hour_start:
                pipe.rename(destination, destination + ':last')
                pipe.rename(start_key, destination + ':pstart')
                pipe.set(start_key, hour_start)

            pipe.zincrby(destination, 1, message)
            log_recent(pipe, name, message, severity, pipe)
            return
        except redis.exceptions.WatchError:
            continue


if __name__ == '__main__':
    # log_recent(redis_conn, 'name', 'message')
    log_common(redis_conn, 'name', 'message')
