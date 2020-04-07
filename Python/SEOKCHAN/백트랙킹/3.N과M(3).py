#!/usr/bin/env python3
# coding: utf-8

from itertools import product

# 중복순열
def main():
    n, m  = map(int, input().split())
    pro = product([ i+1 for i in range(n) ], repeat=m)
    for p in pro:
        print(*p)


if __name__ == '__main__':
    main()

