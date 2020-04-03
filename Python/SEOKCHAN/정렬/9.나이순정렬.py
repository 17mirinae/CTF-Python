#!/usr/bin/env python3
# coding: utf-8

import sys

def main():
    input = lambda: sys.stdin.readline().strip()
    users = []
    for i in range(int(input())):
        tmp = input().split()
        users.append((i, int(tmp[0]), tmp[1]))
    users.sort(key=lambda x: (x[1], x[0]))

    for u in users:
        print(u[1], u[2])


if __name__ == '__main__':
    main()

