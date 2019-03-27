# coding: utf-8
import time
import uuid

from redis_demo import redis_client


def acquire_semaphore(conn, sem_key, limit, timeout=10):
    """
    -inf 表示最小score值; +inf 表示最大score值
    """
    identifier = str(uuid.uuid4())
    now = time.time()

    pipeline = conn.pipeline(True)
    pipeline.zremrangebyscore(sem_key, '-inf', now - timeout)
    pipeline.zadd(sem_key, {identifier: now})
    pipeline.zrank(sem_key, identifier)
    if pipeline.execute()[-1] < limit:
        return identifier
    conn.zrem(sem_key, identifier)
    return None


def release_semaphore(conn, sem_key, identifier):
    """
    正确释放返回true,过期而被删除返回false
    """
    return conn.zrem(sem_key, identifier)


if __name__ == '__main__':
    for i in range(0, 100):
        lock = acquire_semaphore(redis_client.conn, 'semaphore', 5)
        print(lock)
        time.sleep(1)
