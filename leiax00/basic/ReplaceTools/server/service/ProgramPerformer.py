#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

from basic.ReplaceTools.server.dao.ProgramDao import dao, logging
from basic.ReplaceTools.server.service.Processor import *

PROCESSORS = {
    'db': DbProcessor(),
    'pro': ProProcessor(),
    'xml': XmlProcessor()
}


class ProgramPerformer:
    def __init__(self, program_name='prog001'):
        self.program = dao.assemble_program(program_name)

    def execute(self):
        logging.info('change properties start.....')
        for item in self.program.values():
            command = re.match(r'.*_(\w*)\.json', item['serialize_file']).groups()[0]
            PROCESSORS[command].execute(item)


performer = ProgramPerformer()
if __name__ == '__main__':
    performer.execute()
