#!/usr/bin/env python3
# coding: utf-8

def solve(n, m):
    if n < m:
        if m % n == 0:
            return 'factor'
    elif n > m:
        if n % m == 0:
            return 'multiple'
    return 'neither'


def main():
    while True:
        n, m = map(int, input().split())
        if n + m == 0:
            return
        print(solve(n, m))


if __name__ == '__main__':
    main()

