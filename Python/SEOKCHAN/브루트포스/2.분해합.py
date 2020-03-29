#!/usr/bin/env python3
# coding: utf-8

def decomposition(n):
    numbers = list(map(int, list(str(n))))
    return n + sum(numbers)


def solve(n):
    result = []
    for i in range(n - 1, 0, -1):
        if decomposition(i) == n:
            result.append(i)

    if len(result) != 0:
        return result[-1]
    else:
        return 0


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()

