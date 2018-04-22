# coding: utf-8
import re

# test compile()
print('======================test compile()============================')
pattern = re.compile(r'^the', re.I)
pattern1 = re.compile(r'(^the)', re.I)
print(0, pattern.search('Thebbbyrhguigthe'))

# test group() and groups()
print('======================test group() and groups())============================')
gr = pattern.search('the name is leiax00')
gr1 = pattern1.search('the name is leiax00')
print(gr.group())  # the
print(gr.groups())  # ()

print(gr1.group())  # the
print(gr1.groups())  # ('the',)

# test match()
print('======================test match()============================')
match_pattern = re.compile(r'f.o')
m_gr = match_pattern.match('fio')
if m_gr is not None:
    print(m_gr.group())

try:
    print(re.match(r'nam', 'name is leiax00').group())
except AttributeError:
    print('fail to match...')

# test search() and compare match()
print('======================test search() and compare match()============================')
search_pattern = re.compile(r'nam')
print('search', re.search(r'nam', 'the name is leiax00'))  # ('search', <_sre.SRE_Match object at 0x0000000005892718>)
print('match', re.match(r'nam', 'the name is leiax00'))  # ('match', None)

print('pattern search', search_pattern.search('the name is leiax00', 0, 5))  # ('pattern search', None)
print('pattern search', search_pattern.search('the name is leiax00', 0, 15))  # ('pattern search', <_sre.SRE_Match object at 0x0000000005892718>)

print('pattern match', search_pattern.match('the name is leiax00', 0, 5))  # ('pattern match', None)
print('pattern match', search_pattern.match('the name is leiax00', 0, 15))  # ('pattern match', None)

# 匹配多个字符串
print('======================匹配多个字符串============================')
bt = 'bat|bet|bit'  # 正则表达式模式 : bat 、 bet 、 bit
m = re.match(bt, 'bat')  # 'bat'  是一个匹配
if m is not None:
    print('match0', m.group())

m = re.match(bt, 'He bit me!')  # 对于 'blt'  没有匹配
if m is not None:
    print('match1', m.group())

m = re.search(bt, 'He bit me!')  # 通过搜索查找 'bit'
if m is not None:
    print('search', m.group())

# 匹配任何单个字符 -- 点号 `.`
print('======================匹配任何单个字符 -- 点号 `.`============================')
anyend = '.end'
m = re.match(anyend, 'bend')  # 点号匹配 'b'
if m is not None: print(0, m.group())

'bend'
m = re.match(anyend, 'end')  # 不匹配任何字符
if m is not None: print(1, m.group())

m = re.match(anyend, '\nend')  # 除了 \n 之外的任何字符
if m is not None: print(2, m.group())

m = re.search('.end', 'The end.')  # 在搜索中匹配 ' '
if m is not None: print(3, m.group())

# 创建字符集 -- `[]`
print('======================创建字符集 -- `[]`============================')
m = re.match('[cr][23][dp][o2]', 'c3po')  # 匹配 'c3po'
if m is not None: print(1, m.group())  # 'c3po'

m = re.match('[cr][23][dp][o2]', 'c2do')  # 匹配 'c2do'
if m is not None: print(2, m.group())  # 'c2do'

m = re.match('r2d2|c3po', 'c2do')  # 不匹配 'c2do'
if m is not None: print(3, m.group())

m = re.match('r2d2|c3po', 'r2d2')  # 匹配 'r2d2'
if m is not None: print(4, m.group())  # 'r2d2'

# 重复、特殊字符以及分组 -- ？，+， *， （）
print('======================重复、特殊字符以及分组 -- ？，+， *， （）============================')
patt0 = '\w+@(\w+\.)?\w+\.com'  # 任意字母和数字 @ 0个或1个子域名. 主域名.com
patt1 = '\w+@(\w+\.)*\w+\.com'  # 任意字母和数字 @ 任意个子域名. 主域名.com
re.match(patt0, 'nobody@xxx.com').group()
re.match(patt1, 'nobody@www.xxx.yyy.zzz.com').group()

m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print(1, m.group())  # (1, 'abc-123')

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print(2, m.group())  #

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(3, m.group())  # (3, 'abc-123')
print(4, m.groups())  # (4, ('abc', '123'))
print(5, m.group(1))  # (5, 'abc')
print(6, m.group(2))  # (6, '123')

# 使用 findall()和 finditer()查找每一次出现的位置
print('======================使用 findall()和 finditer()查找每一次出现的位置============================')
print(1, re.findall(r'r.*r', 'rcrrcar'))  # (1, ['rcrrcar'])
print(2, re.findall(r'c.r', 'carcur'))  # (2, ['car', 'cur'])

s = 'This and that.'
print(21, re.findall(r'(th\w+) and (th\w+)', s, re.I))  # (21, [('This', 'that')])
print(22, re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().groups())  # (22, ('This', 'that'))
print(23, re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().group(1))  # (23, 'This')
print(24, re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().group(2))  # (24, 'that')
print(25, [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s, re.I)])  # (25, [('This', 'that')])

# 使用 sub()和 subn()搜索与替换
print('======================使用 sub()和 subn()搜索与替换============================')
# attn: Mr. Smith
#
# Dear Mr. Smith,
#
print(re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'))
print(re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'))  # ('attn: Mr. Smith\n\nDear Mr. Smith,\n', 2)
print(re.sub('[ae]', 'X', 'abcdef'))  # XbcdXf
print(re.subn('[ae]', 'X', 'abcdef'))  # ('XbcdXf', 2)
# 使用\N来获取分组的值, N为分组编号, 以下为日期转换
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91'))  # 20/2/91
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991'))  # 20/2/1991

# 在限定模式上使用 split()分隔字符串
print('======================在限定模式上使用 split()分隔字符串============================')
print(re.split(':', 'str1:str2:str3'))  # ['str1', 'str2', 'str3']
print(re.split(':', 'str1:str2:str3', 1)) # ['str1', 'str2', 'str3']

# 扩展符号
print('======================扩展符号============================')
#  re.I/IGNORECASE: 忽略大小写; 写作`?i`
#  re.M/MULTILINE: ^ 和 $ 分别匹配目标字符串中行的起始和结尾,而不是严格匹配整个字符串的起始和结尾; 记作: `?m`
print(1, re.findall(r'(?i)yes', 'yes? Yes. YES!!'))  # (1, ['yes', 'Yes', 'YES'])
f = re.findall(r'(?im)(^th[\w ]+)', """
This line is the first,
another line,
that line, it's the best
""")
print(2, f)  # ['This line is the first', 'that line']

#  re.S/DOTALL : 表明点号（.）能够用来表示\n 符号, 记作`?s`
f = re.findall(r'(?s)th.+', '''
The first line
the second line
the third line
''')
print(3, f)  # (3, ['the second line\nthe third line\n'])

# re.X/VERBOSE 该标记允许用户通过抑制在正则表达式中使用空白符（除了在字符类中或者在反斜线转义中）来创建更易读的正则表达式,就是可以换行。 记作 `?x`
g = re.search(r'''(?x)
\((\d{3})\) #  区号
[ ]
(\d{3})
-
(\d{4})''', '(800) 555-1212').groups()
print(4, g)  # (4, ('800', '555', '1212'))

# (?:…)符号将更流行；通过使用该符号，可以对部分正则表达式进行分组，但是并不会保
# 存该分组用于后续的检索或者应用。当不想保存今后永远不会使用的多余匹配时，这个符号就非常有用。
#  (5, ['google.com', 'google.com', 'google.com'])
print(5, re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com'))
#  (6, [('', 'google.com'), ('www.', 'google.com'), ('code.', 'google.com')])
print(6, re.findall(r'http://(\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com'))

# (?P<name>)通过使用一个名称标识符而不是使用从 1 开始增加到 N 的增量数字来保存匹配，
# 如果使用数字来保存匹配结果，我们就可以通过使用\1,\2 ...,\N \来检索。
# 而对于这种情况可以使用一个类似风格的\g<name>来检索它们。
# (7, {'areacode': '800', 'prefix': '555'})
print(7, re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict())
# 用于搜索替换 (8, '(800) 555-xxxx')
print(8, re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
                '(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212'))

# (?P=name) 可以在一个相同的正则表达式中重用模式，而不必稍后再次在（相同）正则表达式中指定相同的模式。
print(9, re.match(r'(?P<a>\d{3})[-](?P=a)', '999-999').group())  # 999-999
# print(10, re.match(r'(?P<a>\d{3})[-](?P=a)', '999-888').group())  # AttributeError

# (?=...) 正向前视断言  -- L00 lei11 匹配 ' lei', 匹配上则取值 L00
print(10, re.findall(r'\w+(?= lei)', '''L00 lei11
L01 lei12,
L02 lei13
'''))  # (10, ['L00', 'L01', 'L02'])

# (?!…) 负向前视断言
print(11, re.findall(r'(?m)^\s*(?!baidu)(\w+)', '''baidu.com
sina.com, google.com
tecent.cn
'''))  # (11, ['sina', 'tecent'])

print(12, [e.group(1) for e in re.finditer(r'(?m)^\s*(?!baidu)(\w+)', '''baidu.com
sina.com, google.com
tecent.cn
''')])  # (12, ['sina', 'tecent'])

# ?(id/name)Y|N id/name存在则返回Y,否则返回N
print(13, bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))  # (13, True)
print(14, bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))  # (14, False)

