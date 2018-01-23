#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 二三行会多空格
print('''line1
         line2
         line3''')

# 此种方式才是对齐的输出;
print('''line1
line2
line3''')

# 原样输出,不转译
print(r'''hello,\n
world''')

print('''hello,\n
world''')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print('ABC'.encode('ascii'))
