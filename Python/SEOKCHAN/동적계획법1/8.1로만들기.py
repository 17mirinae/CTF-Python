#!/usr/bin/env python3
# coding: utf-8

def solve(n):
    dp = [0] * (n + 1)
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        elif i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(solve(n))

