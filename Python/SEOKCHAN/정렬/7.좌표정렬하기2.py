#!/usr/bin/env python3
# coding: utf-8

def main():
    points = [list(map(int, input().split())) for _ in range(int(input()))]
    points.sort(key=lambda x: (x[1], x[0]))

    for p in points:
        print('{0} {1}'.format(p[0], p[1]))


if __name__ == '__main__':
    main()

