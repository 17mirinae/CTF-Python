#!/usr/bin/env python3
# coding: utf-8

def is_it_in_circle(x, y, r):
    if x ** 2 + y ** 2 <= r ** 2:
        return True
    return False


def d(x1, y1, x2, y2):
    return ( (x1 - x2) ** 2 + (y1 - y2) ** 2 ) ** 0.5


def solve(x1, y1, r1, x2, y2, r2):

    if all([x1 == x2, y1 == y2, r1 == r2]):
        return -1

    distance = d(x1, y1, x2, y2)
    if distance == r1 + r2 or distance == abs(r1 - r2):
        return 1
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        return 0
    else:
        return 2


def main():
    for _ in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(solve(x1, y1, r1, x2, y2, r2))


if __name__ == '__main__':
    main()

