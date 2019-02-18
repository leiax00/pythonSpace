# coding: utf-8
import logging
import time

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


if __name__ == '__main__':
    log_recent(redis_conn, 'name', 'message')
