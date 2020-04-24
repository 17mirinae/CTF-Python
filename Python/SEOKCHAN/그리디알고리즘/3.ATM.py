#!/usr/bin/env python3
# coding: utf-8

def solve(times):
    u = res = 0
    for t in times:
        u += t
        res += u

    return res


def main():
    n = int(input())
    times = list(map(int, input().split()))
    times.sort()
    print(solve(times))


if __name__ == '__main__':
    main()

