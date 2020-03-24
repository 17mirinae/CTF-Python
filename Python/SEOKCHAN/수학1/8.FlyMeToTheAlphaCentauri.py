#!/usr/bin/env python3
# coding: utf-8


"""
distance    path                result
1           1                   1
2           1 1                 2
3           1 1 1               3
4           1 2 1               3
5           1 2 1 1             4
6           1 2 2 1             4
7           1 2 2 1 1           5
8           1 2 2 2 1           5
9           1 2 3 2 1           5
10          1 2 3 2 1 1         6
11          1 2 3 2 2 1         6
12          1 2 3 3 2 1         6
13          1 2 3 3 2 1 1       7
"""

def solve(d):
    i = j = 1
    cnt = 0
    while d > 0:
        d -= i
        i += 1
        cnt += 1
        if d >= j:
            d -= j
            cnt += 1
            j += 1

    return cnt


def main():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(solve(y - x))


if __name__ == '__main__':
    main()

