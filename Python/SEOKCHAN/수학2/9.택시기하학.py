#!/usr/bin/env python3
# coding: utf-8

import math


def solve(r):
    return math.pi * (r ** 2), (r ** 2) * 2


def main():
    r = int(input())
    euclid, taxi = solve(r)
    print(euclid)
    print(taxi)


if __name__ == '__main__':
    main()

