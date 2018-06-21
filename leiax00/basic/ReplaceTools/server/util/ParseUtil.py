#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import json
import logging
import os


def load_json_file(file_path):
    if not os.path.isfile(file_path):
        logging.warn('json file not exist!')
        return False
    with open(file_path, 'r') as j_file:
        load_dict = json.load(j_file)
    print(load_dict)
    return load_dict


def dump_json_file(json_obj, file_path):
    """
    不使用with open是因为无法指定编码，在json固化后无法获取中文，而是ascii编码
    codecs库不会抛出异常
    :param json_obj: 内存中的json对象，一个dict
    :param file_path: json固化到的文件
    """
    fp = codecs.open(file_path, 'w', 'utf-8')
    fp.write(json.dumps(json_obj, ensure_ascii=False, indent=2))
    fp.close()


def parse_xml():
    # todo
    pass


def parse_properties(file_path):
    pro_dict = {}
    if not os.path.isfile(file_path):
        print "properties file not exist!"
        return False
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


if __name__ == '__main__':
    test_file = r'../config/default_pro.json'
    expect_dict = load_json_file(test_file)
    dump_json_file(expect_dict, test_file)
    parse_properties(r'../../temp/root_path/pro.properties')
