#!/usr/bin/env python3
# coding: utf-8

import sys
input = sys.stdin.readline

def solve(n):
    global dp, cost
    for i in range(n):
        if i == 0:
            dp[i][0] = cost[i][0]
            dp[i][1] = cost[i][1]
            dp[i][2] = cost[i][2]

            continue

        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][2], dp[i-1][0])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[n-1][0], dp[n-1][1], dp[-1][2])


if __name__ == '__main__':
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1]*3] * n
    print(solve(n))

