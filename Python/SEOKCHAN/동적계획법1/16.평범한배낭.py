#!/usr/bin/env python3
# coding: utf-8
import sys
input = sys.stdin.readline

def solve(n, w, bags):
    dp = [0] * (w+1)
    for i in range(n):
        for j in range(w, 1, -1):
            if bags[i][0] <= j:
                dp[j] = max(dp[j], dp[j-bags[i][0]] + bags[i][1])

    return dp[-1]


def main():
    n, w = map(int, input().split())
    bags = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, w, bags))


if __name__ == '__main__':
    main()

