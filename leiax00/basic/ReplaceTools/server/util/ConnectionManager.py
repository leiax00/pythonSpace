#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging

import cx_Oracle
import pymysql

from cx_Oracle import OperationalError as o_ex
from pymysql import OperationalError as m_ex
from basic.ReplaceTools.server.bean.ConnectionFindError import ConnectionFindError
from basic.ReplaceTools.start_config import CONFIG, DB_TYPE


class ConnectionManager:
    def __init__(self, config):
        self.config = config
        self.url = self.constructor_url()

    def constructor_url(self):
        return '%(username)s/%(passwd)s@%(ip)s:%(port)i/%(database)s' % self.config

    def get_cursor(self):
        db = None
        try:
            if self.config['db_type'] == DB_TYPE['mysql']:
                db = pymysql.connect(host=self.config['ip'], port=self.config['port'], user=self.config['username'],
                                     password=self.config['passwd'],
                                     database=self.config['database'])
            elif self.config['db_type'] == DB_TYPE['oracle']:
                db = cx_Oracle.connect(self.url)
            return db.cursor()
        except o_ex:
            logging.exception(o_ex)
        except m_ex:
            logging.exception(m_ex)
        finally:
            if db is not None:
                db.close()
        return None


manager = ConnectionManager(CONFIG['db_config'])
if __name__ == '__main__':
    print(manager.constructor_url())
    cursor1 = manager.get_cursor()
    if cursor1 is None:
        logging.warn('cursor is None, can not execute sql...')
        # raise ConnectionFindError('Fail to find a connection.')
    else:
        cursor1.execute('select * from user')
        print(cursor1.fetchone())
