#!/usr/bin/env python3
# coding: utf-8

import sys

def main():
    cnt = [0] * 10001
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        cnt[num] += 1

    for i in range(10001):
        for _ in range(cnt[i]):
            print(i)


if __name__ == '__main__':
    main()

