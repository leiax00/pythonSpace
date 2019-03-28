# coding: utf-8


class CompareData:
    def __init__(self):
        self.param = 'CompareData.py'

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

    def is_equal_for_dict(self, value_1, value_2):
        """ 仅处理字段,列表,字符串,数字这几种类型 """
        print('%s -> method:is_equal_for_dict -> start......' % self.param)
        # todo 未实现
        return True


compare = CompareData()
if __name__ == '__main__':
    pass
