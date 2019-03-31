# coding: utf-8
import threading
import time
import uuid

from redis_demo import redis_client


def acquire_fair_semaphore(sem_name, conn=redis_client.conn, limit=5, timeout=10):
    """
    公平信号量: 兼顾超时,和各客户端时间可能不一致的情况
    :param sem_name:
    :param conn:
    :param limit:
    :param timeout:
    :return:
    """
    identifier = str(uuid.uuid4())
    count_zset = sem_name + ':owner'
    count_key = sem_name + ':counter'

    now = time.time()
    pipeline = conn.pipeline(True)
    pipeline.zremrangebyscore(sem_name, '-inf', now - timeout)
    pipeline.zinterstore(count_zset, {count_zset: 1, sem_name: 0})  # zset交集, 分数相加, 权重0,即不关注该zset的排序

    pipeline.incr(count_key)  # redis本身存储为单线程的,即不存在多线程问题; 但和具体业务掺杂后,就存在事务问题了
    counter = pipeline.execute()[-1]

    pipeline.zadd(sem_name, {identifier: now})
    pipeline.zadd(count_zset, {identifier: counter})

    pipeline.zrank(count_zset, identifier)
    if pipeline.execute()[-1] < limit:
        return identifier, counter

    pipeline.zrem(sem_name, identifier)
    pipeline.zrem(count_zset, identifier)
    pipeline.execute()
    return None, counter


def release_fair_semaphore(sem_name, identifier, conn=redis_client.conn):
    pipeline = conn.pipeline(True)
    pipeline.zrem(sem_name, identifier)
    pipeline.zrem(sem_name + ':owner', identifier)
    return pipeline.execute()[0]


def batch_execute(thread_name, sem_name):
    for j in range(0, 100):
        field, counter = acquire_fair_semaphore(sem_name)
        print('%s -> %d : %s' % (thread_name, counter, field))
        time.sleep(1)


if __name__ == '__main__':
    for i in range(0, 5):
        name = 'thread%d' % i
        threading.Thread(name='name', target=batch_execute, args=(name, 'fair_semaphore')).start()

