#!/usr/bin/env python3
# coding: utf-8
def solve(n):
    dp = [[0] * 10] * 101

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    return sum(dp[n]) % 1000000000


if __name__ == '__main__':
    n = int(input())
    print(solve(n))

