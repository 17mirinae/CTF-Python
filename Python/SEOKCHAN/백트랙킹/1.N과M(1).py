#!/usr/bin/env python3
# coding: utf-8

def solve(n, m):
    result = []

    if m == 1:
        for i in range(1, n + 1):
            result.append([i])
        return result

    while True:
        i = 1
        x = [ 1 ] * m
        while x[-m] < n:
            x[-i] += (x[-i] + 1) % n + 1

            # 중복되는 수가 있는 경우 continue
            if len(x) != len(set(x)):
                continue

            if x[-i] == 1:
                x[-(i + 1)] += 1




    return result


def main():
    n, m = map(int, input().split())
    for s in solve(n, m):
        for i in s:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    main()

