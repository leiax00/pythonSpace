# _*_ coding: utf-8 _*_


def yang_hui(lines):
    line = 0
    line_value = [1]
    while line < lines:
        yield line_value
        a = [1]
        a.extend([v + line_value[k + 1] for k, v in enumerate(line_value) if k != (len(line_value) - 1)])
        a.append(1)
        line_value = a[:]
        line = line + 1


if __name__ == '__main__':
    n = 0
    results = []
    for t in yang_hui(10):
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break

