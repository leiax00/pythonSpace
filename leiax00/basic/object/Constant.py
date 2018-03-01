# __*__ coding: utf-8 __*__


class Constant(object):
    # def __init__(self):
    name = 'leiax00'
    age = 25
    sex = 1

    # def __setattr__(self, key, value):
    #     if key in self.__dict__.keys():
    #         raise self.ConstError("Can't rebind const (%s)" % key)
    #     self.__dict__[key] = value


a = Constant()
if __name__ == '__main__':
    print(a.__dict__)
    a.name = 'lax'
