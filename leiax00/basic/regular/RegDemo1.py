# coding: utf-8
import re


print(1, re.match(r'^the', 'thebbbyrhguigthe'))
print(2, re.search(r'^the', 'thebbbyrhguigthe'))

# 对于要搜寻指定位置或方位的情况下，应该使用搜索模式；否则会导致匹配不正确；
print(3, re.match(r'the$', 'bbbyrhguigthe'))
print(4, re.search(r'the$', 'bbbyrhguigthe'))

print(5, re.match(r'\bthe', 'aa thebbbyrhguig'))
print(6, re.search(r'\bthe', 'aa thebbbyrhguig'))

print(7, re.match(r'\bthe', 'thebbbyrhguig'))
print(8, re.search(r'\bthe', 'thebbbyrhguig'))

print(9, re.match(r'\Bthe', 'thebbbyrhguig'))
print(10, re.search(r'\Bthe', 'thebbbyrhguig'))
print(11, re.search(r'\Bthe', 'AA thebbbyrhguig'))

print(12, re.match(r'\Bthe', 'AAthebbbyrhguig'))
print(13, re.search(r'\Bthe', 'AAthebbbyrhguig'))


# print(re.search(r'^the$', 'the'))
# print(re.match(r'^the$', 'the'))
# print(re.match(r'f.o', 'foo'))
