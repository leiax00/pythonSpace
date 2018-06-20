#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import os

PROJECT_ROOT = r'F:\work_space\pythonSpace\leiax00\basic\ReplaceTools'
LOGGING_PATH = os.path.join(PROJECT_ROOT, r'temp', r'log', r'log.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s line:%(lineno)d)',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=LOGGING_PATH,
                    filemode='w')
DB_TYPE = {
    'mysql': 'mysql',
    'oracle': 'oracle',
}

CONFIG = {
    'root_path': r'F:\work_space\pythonSpace\leiax00\basic\ReplaceTools\root_path',
    'db_config': {
        'db_type': DB_TYPE['mysql'],
        'ip': r'localhost',
        'port': 3305,
        'database': r'ssm',
        'username': r'root',
        'passwd': r'root',
    }
}

print(LOGGING_PATH)
