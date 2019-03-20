# coding: utf-8
import bisect
import random
import uuid

import redis

from redis_demo import redis_client


def add_update_contact(conn, user, contact):
    ac_list = 'recent:' + user
    pipeline = conn.pipeline(True)
    pipeline.lrem(ac_list, contact)
    pipeline.lpush(ac_list, contact)
    pipeline.ltrim(ac_list, 0, 99)  # 保留100个
    pipeline.execute()


def remove_contact(conn, user, contact):
    ac_list = 'recent:' + user
    conn.lrem(ac_list, contact)


def fetch_autocomplete_list(conn, user, sub_str):
    """
    适用于简短列表的自动补全
    """
    ac_list = 'recent:' + user
    contacts = conn.lrange(ac_list, 0, -1)
    fetch_contacts = []
    for contact in contacts:
        if str(contact).startswith(sub_str):
            fetch_contacts.insert(0, contact)  # 以子串开头放首位
        elif sub_str in contact:
            fetch_contacts.append(sub_str)  # 包含放末尾
    return fetch_contacts


def autocomplete_on_prefix(conn, guild, prefix):
    """
    通过有序列表来进行自动补全, 分值均设置为0,则按照名字来排序(仅支持英文字母)
    需要在查询范围前后插入一个新的值,已确定索引上下限,便于查询,完成后移除
    """
    start, end = find_prefix_range(prefix)
    identifier = str(uuid.uuid4())
    start += identifier
    end += identifier
    zset_name = 'members:' + guild

    conn.zadd(zset_name, {start: 0, end: 0})
    pipeline = conn.pipeline(True)
    while 1:
        try:
            pipeline.watch(zset_name)
            start_index = pipeline.zrank(zset_name, start)
            end_index = pipeline.zrank(zset_name, end)
            lrange = min(start_index + 9, end_index - 2)  # 位置从1开始, 索引从0开始, 最大值为 end_index - 2
            pipeline.multi()
            pipeline.zrem(zset_name, start, end)
            pipeline.zrange(zset_name, start_index, lrange)
            items = pipeline.execute()[-1]
            break
        except redis.exceptions.WatchError:
            continue
    return [item.decode('utf-8') for item in items if str('{') not in item.decode('utf-8')]


def join_guild(conn, guild, user):
    conn.zadd('members:' + guild, {user: 0})


def leave_guild(conn, guild, user):
    conn.zrem('members:' + guild, user, 0)


valid_characters = '`abcdefghijklmnopqrstuvwxyz{'  # ascii编码顺序


def find_prefix_range(prefix):
    posn = bisect.bisect_left(valid_characters, prefix[-1:])
    print(posn)
    suffix = valid_characters[(posn or 1) - 1]
    return prefix[:-1] + suffix + '{', prefix + '{'


if __name__ == '__main__':
    # print(find_prefix_range('abd'))
    for i in range(0, 500):
        join_guild(redis_client.conn, 'sword_and_rose', ''.join(random.sample(valid_characters[1:-1], 5)))
    filter_results = autocomplete_on_prefix(redis_client.conn, 'sword_and_rose', 'c')
    print(filter_results)
    redis_client.conn.flushdb()
