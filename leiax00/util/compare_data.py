# coding=utf-8
from abc import ABCMeta


class Custom:
    __metaclass__ = ABCMeta

    def contains(self, other):
        return self.__contains__(other)

    def __eq__(self, other):
        return isinstance(other, Custom) and self.contains(other) and other.contains(self)


class CStr(str, Custom):
    pass


class CList(list, Custom):
    def __contains__(self, item):
        if not isinstance(item, list):
            return False
        for v in item:
            contains = False
            for v1 in self:
                if v1.__contains__(v):
                    contains = True
                    break
            if not contains:
                return False
        return True


class CDict(dict, Custom):
    def __contains__(self, item):
        if not isinstance(item, dict):
            return False
        for k, v in item.items():
            contains = False
            if self.get(k) is not None and self[k].__contains__(v):
                contains = True
            if not contains:
                return False
        return True


def new_custom(data):
    if isinstance(data, dict):
        data = CDict(data)
        for k, v in data.items():
            data[k] = new_custom(v)
    elif isinstance(data, list):
        data = CList(data)
        for index in range(len(data)):
            data[index] = new_custom(data[index])
    else:
        data = CStr(data)
    return data


def contains(data, other):
    return new_custom(data).contains(new_custom(other))


def equal(data, other):
    return new_custom(data) == new_custom(other)


if __name__ == '__main__':
    v1 = CStr('asf')
    l1 = CList('abc')
    l2 = CList(['a', 'b', 'c'])
    print(v1 == l1)
    print(l1 == l2)

    t_data = {'a': 'a1', 'b': ['b1', 'b2'], 'c': {'c1': 'c11', 'c2': 'c22'}, 'd': 2}
    t_data1 = {'a': 'a1', 'b': ['b1', 'b2'], 'd': 2, 'c': {'c1': 'c11', 'c2': 'c22'}}
    t_data = new_custom(t_data)
    t_data1 = new_custom(t_data1)
    print(t_data.contains(t_data1))
    print(t_data == t_data1)
    print(equal(t_data, t_data1))
    print(contains(t_data, t_data1))
