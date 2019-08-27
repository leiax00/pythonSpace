# coding=utf-8
import redis


class CONFIG:
    HOST = 'localhost'
    PORT = '6379'
    PASSWORD = 'root'


# 对于每一个Redis服务器，用户只需要创建一个conn对象
conn = redis.Redis(host=CONFIG.HOST, port=CONFIG.PORT, password=CONFIG.PASSWORD)
