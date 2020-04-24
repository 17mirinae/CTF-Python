#!/usr/bin/env python3
# coding: utf-8

def solve(n, k, coins):
    cnt = 0
    for coin in coins[::-1]:
        if coin <= k:
            s = k // coin
            k -= coin * s
            cnt += s

    return cnt


def main():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    print(solve(n, k, coins))


if __name__ == '__main__':
    main()

