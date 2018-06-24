#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import functools
import json
import logging
import os
import re

from basic.ReplaceTools.start_config import PROJECT_ROOT


def check_file(index):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if not os.path.isfile(args[index]):
                logging.error(r'properties file not exist')
                return
            return func(*args, **kw)

        return wrapper

    return decorator


@check_file(0)
def load_json_file(file_path):
    with open(file_path, 'r') as j_file:
        load_dict = json.load(j_file)
    for k, v in load_dict.items():
        load_dict[k] = dict({'serialize_file': file_path}, **v)
    return load_dict


def dump_json_file(json_obj):
    """
    不使用with open是因为无法指定编码，在json固化后无法获取中文，而是ascii编码
    codecs库不会抛出异常
    :param json_obj: 新增的一个独立方案，一个dict，包括配置，和序列化的文件路径（key: serialize_file）
        结构： ｛key:{配置, 'serialize_file': 序列化路径｝
    """
    for k, v in json_obj.items():
        serialize_file = v.pop('serialize_file')
        if not os.path.isfile(serialize_file):
            logging.warn('serialize_file not exist!')
            continue
        with open(serialize_file, 'r') as j_file:
            load_dict = json.load(j_file)
        fp = codecs.open(serialize_file, 'w', 'utf-8')
        load_dict[k] = v
        fp.write(json.dumps(load_dict, ensure_ascii=False, indent=2))
        fp.close()


def parse_xml():
    # todo
    pass


@check_file(0)
def parse_properties(file_path):
    pro_dict = {}
    try:
        pro_file = open(file_path, "r")
        for line in pro_file.readlines():
            line = line.strip(' \t\n')
            if line and not line.startswith("#"):
                print line
                temp = line.split("=")
                temp[0] = temp[0].strip(' \t\n')
                temp[1] = temp[1].strip(' \t\n')
                pro_dict[temp[0]] = temp[1]
    except Exception, e:
        logging.exception('Fail to load properties', e)
    else:
        pro_file.close()
    print(pro_dict)
    return pro_dict


def get_file_by_reg(reg_exp):
    match_list = []
    for (root, dirs, files) in os.walk(PROJECT_ROOT):
        for temp in files:
            if re.match(reg_exp, temp):
                match_list.append(os.path.join(root, temp))
    return match_list


def get_schemes(reg_exp, parse_method):
    schemes = {}
    files = get_file_by_reg(reg_exp)
    for temp_file in files:
        schemes = dict(parse_method(temp_file), **schemes)
    return schemes


if __name__ == '__main__':
    # print(get_file_by_reg(r'.*_db\.json'))
    # test_file = r'../config/default_pro.json'
    # expect_dict = load_json_file(test_file)
    program = {u'pro002': {u'change_config': [{u'target_label': u'org.leiax00.pro02', u'target_value': u'xxxxx'}],
                           'serialize_file': '../config/default_pro.json', u'target_file': u'pro.properties'}}
    dump_json_file(program)
    # parse_properties(r'../../temp/root_path/pro.properties')
