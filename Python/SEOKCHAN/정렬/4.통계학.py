#!/usr/bin/env python3
# coding: utf-8

import sys
import statistics as st
from collections import Counter


def mean(nums):
    return round(sum(nums) / len(nums))

def proper_round(num, dec=0):
    num = float(num)
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])


def mid(nums):
    nums.sort()
    return nums[len(nums) // 2]


def most_common(nums):
    if len(nums) == 1:
        return nums[0]

    c = Counter(nums)
    tmp = c.most_common()

    if tmp[0][1] == tmp[1][1]:
        return tmp[1][0]
    else:
        return tmp[0][0]


def main():
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(mean(nums))
    print(mid(nums))
    print(most_common(nums))
    print(max(nums) - min(nums))


if __name__ == '__main__':
    main()

