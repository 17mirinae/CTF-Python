#!/usr/bin/env python3
# coding: utf-8

def check(a, b, v, days):
    tmp = (a - b) * (days - 1)
    if (a - b) * (days - 1) + a >= v:
        return True
    return False


def solve(a, b, v):
    top = 1000000001
    bottom = 1
    while True:
        middle = (top + bottom) // 2
        # print('top :', top, '| middle :', middle, '| bottom :', bottom)
        res1 = check(a, b, v, middle)
        res2 = check(a, b, v, middle - 1)
        if res1 is True and res2 is False:
            return middle
        elif res1 is True and res2 is True:
            top = middle - 1
        else:
            bottom = middle + 1


def main():
    a, b, v = map(int, input().split())
    print(solve(a,b,v))


if __name__ == '__main__':
    main()

