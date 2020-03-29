#!/usr/bin/env python3
# coding: utf-8

def fibo(x):
    if x in [0, 1]:
        return x
    return fibo(x-1) + fibo(x-2)


def main():
    n = int(input())
    print(fibo(n))


if __name__ == '__main__':
    main()

