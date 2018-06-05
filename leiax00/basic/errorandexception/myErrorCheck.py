# __*__ coding: utf-* __*__
from basic.errorandexception.myError import MyError


class MyErrorCheck:
    def __init__(self):
        pass

    @staticmethod
    def error_check():
        try:
            raise MyError(1024, 'my error happen')
        except MyError as e:
            print(e.error_msg)
        else:
            print('no error')
        finally:
            print('finally...')


if __name__ == '__main__':
    my = MyErrorCheck()
    my.error_check()
    n = 0
    assert n != 0, 'n is zero!'
