#!/usr/bin/env python3
# coding: utf-8


def solve(i, num, add, sub, mul, div):
    global n, nums, max_num, min_num
    if i == n:
        max_num = max([num, max_num])
        min_num = min([num, min_num])
        return

    else:
        if add:
            solve(i + 1, num + nums[i], add - 1, sub, mul, div)
        if sub:
            solve(i + 1, num - nums[i], add, sub - 1, mul, div)
        if mul:
            solve(i + 1, num * nums[i], add, sub, mul - 1, div)
        if div:
            solve(i + 1, int(num / nums[i]), add, sub, mul, div - 1)



def main():
    global n, nums, max_num, min_num
    n = int(input())
    nums = list(map(int, input().split()))
    ope = list(map(int, input().split()))

    max_num = -1000000000
    min_num = max_num * -1
    solve(1, nums[0], * ope)
    print(max_num)
    print(min_num)


if __name__ == '__main__':
    main()

