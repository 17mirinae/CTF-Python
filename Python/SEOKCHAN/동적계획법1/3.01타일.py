#!/usr/bin/env python3
# coding: utf-8

def solve(n):
    v1 = 1
    v2 = 2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    s = v1 + v2
    for i in range(3, n + 1):
        s = (v1 + v2) % 15746
        v1 = v2
        v2 = s
    return s

def main():
    n = int(input())
    s = solve(n)
    print(s)


if __name__ == '__main__':
    main()

