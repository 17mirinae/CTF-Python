#!/usr/bin/env pypy3
# coding: utf-8


def set_depth(layer):
    depth = [0, ]
    tiles = 1
    for i in range(0, layer):
        tiles += i * 6
        depth.append(tiles)
    return depth


def solve(n):
    depth = set_depth(18258)        # N <= 1000000000
    i = 1
    while True:
        tiles = depth[i]
        if n <= tiles:
            return i
        i += 1


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()

