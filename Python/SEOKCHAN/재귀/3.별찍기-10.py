#!/usr/bin/env python3
# coding: utf-8
def draw(x, y):
    while y != 0:
        if x % 3 == 1 and y % 3 == 1:
            print(" ", end="")
            return
        x = x // 3
        y = y // 3
    print("*", end="")


def solve(n):
    for y in range(n):
        for x in range(n):
            draw(x, y)
        print()


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()

