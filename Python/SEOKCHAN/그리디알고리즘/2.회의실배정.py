#!/usr/bin/env python3
# coding: utf-8

def solve(meetings):
    start = cnt = 0
    for m in meetings:
        if m[0] >= start:
            start = m[1]
            cnt += 1

    return cnt


def main():
    n = int(input())
    meetings = [list(map(int, input().split())) for _ in range(n)]
    meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    print(solve(meetings))


if __name__ == '__main__':
    main()

