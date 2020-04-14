#!/usr/bin/env python3
# coding: utf-8

result = [0] * 91
def solve(n):
    global result
    if n <= 2:
        return 1
    if result[n] == 0:
        result[n] = solve(n - 1) + solve(n - 2)

    return result[n]


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()

