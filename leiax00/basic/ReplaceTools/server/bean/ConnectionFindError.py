#!/usr/bin/python
# -*- coding: UTF-8 -*-


class ConnectionFindError(Exception):
    def __init__(self, error_code=None, error_msg=None):
        Exception.__init__(self)
        self.error_code = error_code
        self.error_msg = error_msg
