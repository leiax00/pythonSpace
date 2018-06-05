# __*__ coding: utf-* __*__


class MyError(Exception):
    def __init__(self, error_code, error_msg):
        Exception.__init__(self)
        self.error_code = error_code
        self.error_msg = error_msg