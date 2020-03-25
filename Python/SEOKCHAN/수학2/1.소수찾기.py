#!/usr/bin/env python3
# coding: utf-8

def solve(num_list):
    max_num = max(num_list)
    nums = [True for i in range(0, max_num+1)]
    nums[0] = nums[1] = False
    for i in range(0, max_num + 1):
        if nums[i] is False:
            continue
        j = 2
        while j * i <= max_num:
            nums[i * j] = False
            j += 1
    res = 0
    for num in num_list:
        if nums[num] is True:
            res += 1
    return res


def main():
    input()
    num_list = list(map(int, input().split()))
    print(solve(num_list))


if __name__ == '__main__':
    main()

