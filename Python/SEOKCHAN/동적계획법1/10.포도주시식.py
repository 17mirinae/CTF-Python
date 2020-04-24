#!/usr/bin/env python3
# coding: utf-8

def solve(wines):
    dp = [0] * (n + 10)
    dp[1] = wines[1]
    dp[2] = wines[1] + wines[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i], dp[i-1])
        print(i, dp[i])

    return dp[n]

if __name__ == '__main__':
    n = int(input())
    wines = [0] + [int(input()) for _ in range(n)]
    print(solve(wines))

