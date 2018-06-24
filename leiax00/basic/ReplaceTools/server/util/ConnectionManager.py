#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
from cx_Oracle import OperationalError as o_ex

import cx_Oracle
import pymysql
from pymysql import OperationalError as m_ex

from basic.ReplaceTools.config.start_config import CONFIG, DB_TYPE


class ConnectionManager:
    def __init__(self, config):
        self.config = config
        self.url = self.constructor_url()

    def constructor_url(self):
        return '%(username)s/%(passwd)s@%(ip)s:%(port)i/%(database)s' % self.config

    def get_connection(self):
        conn = None
        try:
            if self.config['db_type'] == DB_TYPE['mysql']:
                conn = pymysql.connect(host=self.config['ip'], port=self.config['port'], user=self.config['username'],
                                     password=self.config['passwd'],
                                     database=self.config['database'])
            elif self.config['db_type'] == DB_TYPE['oracle']:
                conn = cx_Oracle.connect(self.url)
        except o_ex:
            logging.exception(o_ex)
        except m_ex:
            logging.exception(m_ex)
        return conn


manager = ConnectionManager(CONFIG['db_config'])
if __name__ == '__main__':
    print(manager.constructor_url())
    cursor1 = manager.get_cursor()
    if cursor1 is None:
        logging.warn('cursor is None, can not execute sql...')
        # raise ConnectionFindError('Fail to find a connection.')
    else:
        cursor1.execute('UPDATE `user` SET userAge = 666 WHERE id = 2')
        # print(cursor1.fetchone())
        cursor1.close()
