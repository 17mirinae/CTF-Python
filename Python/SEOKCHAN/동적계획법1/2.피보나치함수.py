#!/usr/bin/env python3
# coding: utf-8

import sys
input = sys.stdin.readline

result = [0] * 91
result[0] = 0
result[1] = 1
result[-1] = 1
def solve(n):
    global result
    if n < 2:
        return result[n]
    else:
        if result[n] == 0:
            result[n] = solve(n - 1) + solve(n - 2)
        return result[n]


def main():
    global result
    for _ in range(int(input().strip())):
        n = int(input().strip())
        solve(n)
        print(result[n - 1], result[n])


if __name__ == '__main__':
    main()

