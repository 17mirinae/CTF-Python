#!/usr/bin/env python3
# coding: utf-8

# Euclidean algorithm
def gcd(x, y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y


def solve(n, m):
    g = gcd(n, m)
    lcm = n * m // g
    return g, lcm


def main():
    n, m = map(int, input().split())
    g, l = solve(n, m)

    print(g, l, sep='\n')


if __name__ == '__main__':
    main()

