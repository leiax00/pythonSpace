#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import os

from basic.ReplaceTools.server.util.ConnectionManager import ConnectionManager
from basic.ReplaceTools.server.util.XmUtil import *
from basic.ReplaceTools.start_config import CONFIG


class Processor(object):
    def execute(self, change_entity):
        pass


class DbProcessor(Processor):
    def execute(self, change_entity):
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
                logging.info('db Processor execute success....')
            finally:
                conn.close()


class ProProcessor(Processor):
    def execute(self, change_entity):
        targets = [target for target in change_entity['change_config']]
        target_file = os.path.join(CONFIG['root_path'], change_entity['target_file'])
        self.__modify_item(target_file, targets)

    @staticmethod
    def __modify_item(target_file, targets):
        try:
            open_f = open(target_file, "r")
            lines = open_f.readlines()
            for i in range(0, len(lines)):
                line = lines[i].strip(' \t\n')
                if not line or line.startswith("#"):
                    continue
                key = line.split('=')[0].strip(' \t\n')
                for target in targets:
                    if key == target['target_label']:
                        lines[i] = '%s=%s\n' % (key, target['target_value'])
            write_f = open(target_file, "w")
            print('write lines: %s' % lines)
            write_f.writelines(lines)
        except Exception, e:
            logging.exception(('Fail to load properties: %s', e))
            raise e
        else:
            open_f.close()
            write_f.close()


class XmlProcessor(Processor):
    def __init__(self):
        self.change_entity = {}
        self.file_path = ''

    def execute(self, change_entity):
        self.change_entity = change_entity
        self.file_path = os.path.join(CONFIG['root_path'], change_entity['target_file'])
        self.change_value()
        self.add_child()

    def change_value(self):
        """
        该方法判断逻辑：获取‘target_tag’第一级子节点，然后根据唯一标识key，获取到；
        再根据后续层级获得需要修改的标签
        :return:
        """
        try:
            tree = read_xml(self.file_path)
            for change in self.change_entity['change_child']:
                result_nodes = self.__get_target_nodes(tree, change)
                change_node_text(result_nodes, change['target_value'])
            write_xml(tree, self.file_path)
        except IOError, e:
            logging.exception(e)
            return False
        else:
            return True

    def add_child(self):
        tree = read_xml(self.file_path)
        for child in self.change_entity['add_child']:
            result_nodes = self.__get_target_nodes(tree, child)
            node_list = []
            for node_attr in child['new_node']:
                node_list.append(create_node(node_attr['tag'], node_attr['attrs'], node_attr['text_value']))
            for new_node in node_list:
                add_child_node(result_nodes, new_node)
        write_xml(tree, self.file_path)

    @staticmethod
    def __get_target_nodes(tree, node_path):
        tags = node_path['target_tag'].split('/', 1)
        nodes = get_node_by_key(find_nodes(tree, tags[0]), {node_path['key']: node_path['key_value']})
        result_nodes = []
        for node in nodes:
            result_nodes.extend(find_nodes(node, tags[1]))
        return result_nodes
