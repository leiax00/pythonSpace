# __*__ coding: utf-8 __*__


class Field(object):
    __type__ = object

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def check(self, param):
        if not isinstance(param, self.__type__):
            print('%s is invalid!' % param)
        print('check %s success!!!' % param)

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    __type__ = str

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    __type__ = int

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
