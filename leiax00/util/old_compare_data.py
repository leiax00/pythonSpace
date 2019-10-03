# coding: utf-8
"""
类的方式要在RF中调用,需要配置成模块; 或者使文件名和类名一致才可, 否则只能以方法的方式来调用;
疑惑: 根据规范文件名是下划线的方式,而类名是驼峰模式; 那么RF是否是不推荐直接引用文件的方式?
但部署过程中要把直接的python代码作为第三方库放入sites-package中是否更加困难?
因此对于中小型的项目是否应该以单个脚本为主,切尽量使用模块的方式而不是类的方式?
"""


def is_equal_for_list(list_1, list_2):
    return CompareData().is_equal_for_dict(list_1, list_2)


def is_equal_for_dict(dict_1, dict_2):
    return CompareData().is_equal_for_dict(dict_1, dict_2)


class CompareData:
    def __init__(self):
        self.param = 'old_compare_data.py'

    def is_equal_for_list(self, list_1, list_2):
        """ 仅处理字段,列表,字符串,数字这几种类型 """
        print('%s -> method:is_equal_for_list -> start......' % self.param)
        if not isinstance(list_1, list) or not isinstance(list_2, list):
            return False
        if len(list_1) != len(list_2):
            return False
        for value_1 in list_1:
            if isinstance(value_1, dict):
                is_success = False
                for value_2 in list_2:
                    if isinstance(value_2, dict):
                        is_success = self.is_equal_for_dict(value_1, value_2)
                if not is_success:
                    return False
            elif isinstance(value_1, list):
                is_success = False
                for value_2 in list_2:
                    if isinstance(value_2, list):
                        is_success = self.is_equal_for_list(value_1, value_2)
                if not is_success:
                    return False
            else:  # string
                is_success = False
                for value_2 in list_2:
                    if str(value_1) == str(value_2):
                        is_success = True
                        break
                if not is_success:
                    return False
        return True

    def is_equal_for_dict(self, dict_1, dict_2):
        """ 仅处理字段,列表,字符串,数字这几种类型 """
        print('%s -> method:is_equal_for_dict -> start......' % self.param)
        # todo 未实现
        return True


compare = CompareData()
if __name__ == '__main__':
    pass
