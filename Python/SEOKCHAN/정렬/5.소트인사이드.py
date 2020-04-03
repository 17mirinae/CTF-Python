#!/usr/bin/env python3
# coding: utf-8

def main():
    n = input()
    nums = list(map(int, list(n)))
    nums.sort(reverse=True)
    res = ''
    for i in nums:
        res += str(i)
    print(res)


if __name__ == '__main__':
    main()

