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
