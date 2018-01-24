# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
K = L[:]
K[0] = 'a'
print(L)
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

alist = []
for temp in range(10, 0, -2):
    alist.append(temp)

print(alist)

tolist = list('hallo, world!')
print(tolist)
del tolist[5]
print(''.join(tolist))


def print_box(left_margin, box_width, box_high):
    high = 0
    print()
    print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
    while high < box_high-2:
        print(' ' * left_margin + '|' + ' ' * (box_width-2) + '|')
        high = high + 1
    print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')


if __name__ == '__main__':
    print_box(10, 100, 10)
