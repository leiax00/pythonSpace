# coding: utf-8
"""
这种分文件的脚本,在rf中使用必须配置pythonpath才可以正常运行, 及执行robot的时候要添加 --pythonpath 参数
"""
from python.temp.next_step import second_step


def first_method():
    second_step()
