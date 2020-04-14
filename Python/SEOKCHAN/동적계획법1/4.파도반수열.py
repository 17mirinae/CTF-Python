#!/usr/bin/env python3
# coding: utf-8

result = [0] * 101
def solve(n):
    if n < 4:
        return 1
    else:
        if result[n] == 0:
            result[n] = solve(n - 2) + solve(n - 3)
        return result[n]


def main():
    for _ in range(int(input())):
        n = int(input())
        print(solve(n))


if __name__ == '__main__':
    main()

