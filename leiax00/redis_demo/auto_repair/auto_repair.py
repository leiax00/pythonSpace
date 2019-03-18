# coding: utf-8
import bisect


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
    pass


valid_characters = '`abcdefghijklmnopqrstuvwxyz{'  # ascii编码顺序


def find_prefix_range(prefix):
    posn = bisect.bisect_left(valid_characters, prefix[-1:])
    print(posn)
    suffix = valid_characters[(posn or 1) - 1]
    return prefix[:-1] + suffix + '{', prefix + '{'


if __name__ == '__main__':
    print(find_prefix_range('abd'))
