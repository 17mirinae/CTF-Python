#!/usr/bin/env python3
# coding: utf-8


def get_fraction(n):
    fractions = []
    for i in range(1, n + 1):
        if n % 2 == 0:
            fractions.append('{0}/{1}'.format(i, n - (i - 1)))
        else:
            fractions.append('{0}/{1}'.format(n - (i - 1), i))
    return fractions


def solve(n):
    len_fractions = 0
    i = 1
    while True:
        len_fractions += i
        if n <= len_fractions:
            fractions = get_fraction(i)
            return fractions[n - len_fractions + i - 1]
        i += 1

def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()

