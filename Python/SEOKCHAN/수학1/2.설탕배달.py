#!/usr/bin/env python3


def solve(n):
    solution = []
    for i in range(0, n // 5 + 1):
        remainder = n - (5 * i)
        if remainder % 3 == 0:
            n3 = remainder // 3
            n5 = i
            solution.append((n3, n5))
    try:
        return min([i for i in map(sum, solution)])
    except:
        return -1


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()

