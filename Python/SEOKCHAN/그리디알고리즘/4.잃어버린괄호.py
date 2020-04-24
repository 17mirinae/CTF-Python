#!/usr/bin/env python3
# coding: utf-8

import re

def solve(nums):
    while len(nums) > 1:
        for i in nums:
            if i < 0:

    return


def main():
    expression = input()
    expression = re.sub('(-|\+)', ' \g<0>', expression)
    nums = list(map(int, expression.split(' ')))
    print(solve(nums))


if __name__ == '__main__':
    main()

