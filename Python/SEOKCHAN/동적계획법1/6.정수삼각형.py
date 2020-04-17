#!/usr/bin/env python3
# coding: utf-8

import sys
input = sys.stdin.readline

def solve(triangle):
    for i in range(n):
        if i == 0:
            continue
        elif i == 1:
            for j in range(2):
                triangle[i][j] += triangle[0][0]
            continue

        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])


if __name__ == '__main__':
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, input().split())))

    print(solve(triangle))

