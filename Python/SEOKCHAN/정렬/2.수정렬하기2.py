#!/usr/bin/env python3
# coding: utf-8

import sys

def main():
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().strip()))]
    nums.sort()
    for n in nums:
        print(n)

if __name__ == '__main__':
    main()

