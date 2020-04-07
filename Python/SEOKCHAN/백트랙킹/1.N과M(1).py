#!/usr/bin/env python3
# coding: utf-8

from itertools import permutations

def main():
    n, m = map(int, input().split())
    per = permutations([i + 1 for i in range(n)], m)
    for p in list(per):
        for k in p:
            print(k, end=' ')
        print()




if __name__ == '__main__':
    main()


