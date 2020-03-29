#!/usr/bin/env python3
# coding: utf-8

def factorial(x):
    if x in [0, 1]:
        return 1
    return x * factorial(x - 1)


def main():
    n = int(input())
    print(factorial(n))


if __name__ == '__main__':
    main()

