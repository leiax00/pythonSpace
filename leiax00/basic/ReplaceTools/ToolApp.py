#!/usr/bin/python
# -*- coding: UTF-8 -*-
from basic.ReplaceTools.server.service.ProgramPerformer import performer
from basic.ReplaceTools.start_config import *


class ToolMain:

    def __init__(self):
        print_box(10, 80, 9)
        self.performer = performer

    def start(self, program_key=None):
        self.performer.set_program(program_key)
        self.performer.execute()


app = ToolMain()
if __name__ == '__main__':
    app.start('prog002')
