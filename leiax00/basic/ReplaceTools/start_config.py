#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import os

# **********************************系统属性配置*************************************
PROJECT_ROOT = r'F:\work_space\pythonSpace\leiax00\basic\ReplaceTools'
DB_TYPE = {
    'mysql': 'mysql',
    'oracle': 'oracle',
}
# **********************************环境属性配置*************************************
CONFIG = {
    'root_path': r'F:\work_space\pythonSpace\leiax00\basic\ReplaceTools\temp\root_path',
    'db_config': {
        'db_type': DB_TYPE['mysql'],
        'ip': r'localhost',
        'port': 3306,
        'database': r'ssm',
        'username': r'root',
        'passwd': r'root',
    }
}
# **********************************日志属性配置*************************************
LOGGING_PATH = os.path.join(PROJECT_ROOT, r'temp', r'log', r'log.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s line:%(lineno)d)',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=LOGGING_PATH,
                    filemode='w')


def print_box(left_margin, box_width, box_high):
    high = 0
    print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
    while high < box_high - 2:
        if 2 * high == box_high - 5:
            s = '欢迎使用本工具'
            space_num = ((box_width - len(s)) / 2 + 3)
            print(' ' * left_margin + '|' + ' ' * space_num + s + ' ' * space_num + '|')
        elif 2 * high == box_high + 1:
            s = '@不存在的界面'
            space_num = box_width - len(s) -3
            print(' ' * left_margin + '|' + ' ' * space_num + s + ' ' * 7 + '|')
        elif 2 * high == box_high + 3:
            s = 'by 雷翱翔 & 杨正勇'
            space_num = box_width - len(s) + 2
            print(' ' * left_margin + '|' + ' ' * space_num + s + ' ' * 2 + '|')
        else:
            print(' ' * left_margin + '|' + ' ' * (box_width - 2) + '|')
        high = high + 1
    print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
