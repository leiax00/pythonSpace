# coding: utf-8
import time
import uuid


def acquire_lock(conn, lock_name, acquire_timeout=10):
    """
    获取锁: 通过setnx来写一个不存在的key作为锁
    setnx:这个明明只会在键不存在的情况下设置值
    """
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_timeout
    while time.time() < end:
        if conn.setnx('lock:' + lock_name, identifier):
            return identifier
        time.sleep(.001)
    return False


def release_lock(conn, lock_name, locked):
    if not locked:
        conn.delete('lock:%s' % lock_name)


def purchase_item_with_lock(conn, buyer_id, item_id, seller_id):
    """
    简易加锁的买卖场景:从商城买, 买家得物品扣金钱,买家得金钱,商城扣除商品
    """
    buyer = 'users:%s' % buyer_id
    seller = 'users:%s' % seller_id
    item = "%s.%s" % (item_id, seller_id)
    buyer_inventory = 'inventory:%s' % buyer_id
    lock_name = "market:%s" % item

    locked = acquire_lock(conn, lock_name)
    if not locked:
        return False
    pipe = conn.pipeline(True)
    try:
        pipe.zscore('market:', item)
        pipe.hget(buyer, 'funds')
        price, funds = pipe.execute()
        if price is None or price > funds:
            return None
        pipe.hincrby(seller, 'funds', int(price))
        pipe.hincrby(buyer, 'funds', int(-price))
        pipe.sadd(buyer_inventory, item_id)
        pipe.zrem('market:', item)
        pipe.execute()
        return True
    finally:
        release_lock(conn, lock_name, locked)
