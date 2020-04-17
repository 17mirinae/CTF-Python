#!/usr/bin/env python3
# coding: utf-8

import sys
input = sys.stdin.readline


def solve(stairs):
    dp = [0] * n

    for i in range(n):
        if i == 0:
            dp[0] = stairs[0]
            continue
        elif i == 1:
            dp[1] = max(stairs[0] + stairs[1], stairs[1])
            continue
        elif i == 2:
            dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
            continue
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    return dp[-1]


if __name__ == '__main__':
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    print(solve(stairs))

