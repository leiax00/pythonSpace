# coding: utf-8
import time

from redis_demo.RedisClient import redis_conn

ONE_MINUTE = 60

ONE_HOUR = 60 * 60

PRECISION = [1, 5, ONE_MINUTE, 5 * ONE_MINUTE, ONE_HOUR, 5 * ONE_HOUR, 24 * ONE_HOUR]


def update_counter(conn=redis_conn, name='', count=1, now=None):
    now = now or time.time()
    pipe = conn.pipeline()
    for perc in PRECISION:
        p_now = int(now / perc) * perc
        value = '%s:%s' % (perc, name)
        pipe.zadd('known', {value: 0})  # 当分值为0时，value来进行排序（不是整个value，而是从第一个字符开始对比）
        pipe.hincrby('count:%s' % value, p_now, count)
    pipe.execute()


def get_counter(conn, name, precision):
    value = '%s:%s' % (precision, name)
    data = conn.hgetall('count:%s' % value)
    return_value = []
    for key, v in data.items():
        return_value.append((int(key), int(v)))
    return_value.sort()
    return return_value


if __name__ == '__main__':
    name = 'leiax00'
    update_counter(name=name)
    return_v = get_counter(redis_conn, name, 5)
    print(return_v)
