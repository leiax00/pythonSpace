#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging

from basic.ReplaceTools.server.util.ConnectionManager import ConnectionManager


class Processor(object):
    def execute(self, change_entity):
        pass


class DbProcessor(Processor):
    def execute(self, change_entity):
        print('DbProcessor: %s' % change_entity)
        manager = ConnectionManager(change_entity['db_config'])
        conn = manager.get_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                for sql in change_entity['sql']:
                    cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                logging.warn('db Processor execute failure....')
            else:
                logging.info('db Processor execute finished....')
            finally:
                conn.close()


class ProProcessor(Processor):
    def execute(self, change_entity):
        print('ProProcessor: %s' % change_entity)


class XmlProcessor(Processor):
    def execute(self, change_entity):
        print('XmlProcessor: %s' % change_entity)
