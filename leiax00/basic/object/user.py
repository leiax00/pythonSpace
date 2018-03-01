# __*__ coding: utf-8 __*__
from leiax00.basic.object.Constant import Constant


class User(Constant):

    def to_string(self):
        return 'name: %s, age: %s, sex: %s.' % (self.name, self.age, self.sex)

    def __str__(self):
        return 'name: %s, age: %s, sex: %s.' % (self.name, self.age, self.sex)


user = User()
if __name__ == '__main__':
    print(user.to_string())
    print(user)  # 调用 __str__(self)方法
    user.name = 'aaa'
    print(Constant.name)
    print(user.name)  # 覆盖继承下来的类变量
    del user.name  # 删除实例变量后, 重新显示类变量
    print(user.name)
