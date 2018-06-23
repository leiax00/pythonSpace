#!/usr/bin/python
# -*- coding: UTF-8 -*-
from basic.ReplaceTools.server.util.FileUtil import *

DB_REG = r'.*_db\.json'
PRO_REG = r'.*_pro\.json'
XML_REG = r'.*_xml\.json'
PROGRAM_REG = r'Program.json'


class ProgramDao:
    def __init__(self):
        self.db_schemes = get_schemes(DB_REG, load_json_file)
        self.pro_schemes = get_schemes(PRO_REG, load_json_file)
        self.xml_schemes = get_schemes(XML_REG, load_json_file)
        self.programs = get_schemes(PROGRAM_REG, load_json_file)
        self.all_schemes = dict(self.db_schemes.items() + self.pro_schemes.items() + self.xml_schemes.items())

    def assemble_program(self, program_name):
        cur_program = {}
        for key in self.programs[program_name]['items']:
            cur_program = dict({key: self.all_schemes[key]}, **cur_program)
        return cur_program

    def dump_program(self, new_program):
        next_index = self.generate_key(self.programs.keys())
        self.programs[next_index] = new_program
        dump_json_file(self.programs)

    @staticmethod
    def generate_key(key_list):
        max_index = max(key_list)
        suffix = re.match(r'prog([0-9]*)', max_index).groups()[0]
        return '%s%03i' % ('prog', int(suffix) + 1)


dao = ProgramDao()
if __name__ == '__main__':
    print(dao.generate_key(['prog001', 'prog002']))
    print(dao.db_schemes)
    print(dao.assemble_program('prog001'))
