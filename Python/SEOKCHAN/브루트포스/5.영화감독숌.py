#!/usr/bin/env python3
# coding: utf-8

def solve(n):
    i = 666
    order = 0
    while True:
        if str(i).find('666') > -1:
            order += 1
            if order == n:
                return i
        i += 1


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()

