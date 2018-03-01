# __*__ coding: utf-8 __*__
from leiax00.basic.object.orm_model.Filed import *
from leiax00.basic.object.orm_model.Model import Model


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    print(u.id)
    # del u.id
    # print(u.id)
    u.save()

'''
通过上述方式, 相当于固定了当前类的属性, 可让其作为一个数据entity对象, 和数据库的交互上不会受到python机制的影响;
(python的对象可以无限的外挂实例属性上去, 导致和数据库的映射关系较复杂)

'''