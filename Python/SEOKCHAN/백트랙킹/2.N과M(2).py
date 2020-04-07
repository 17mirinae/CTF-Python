#!/usr/bin/env python3
# coding: utf-8

from itertools import combinations

# 중복조합
def main():
    n, m = map(int, input().split())
    com = combinations([i + 1 for i in range(n)], m)
    for c in list(com):
        print(* c)


if __name__ == '__main__':
    main()

