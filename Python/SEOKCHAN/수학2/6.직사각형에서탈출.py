#!/usr/bin/env python3
# coding: utf-8

def solve(x, y, w, h):
    return min([x, y, w - x, h - y])


def main():
    x, y, w, h = map(int, input().split())
    print(solve(x, y, w, h))


if __name__ == '__main__':
    main()

