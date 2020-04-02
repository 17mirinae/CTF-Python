#!/usr/bin/env python3
# coding: utf-8

def main():
    numbers = []
    for _ in range(int(input())):
        numbers.append(int(input()))

    numbers.sort()
    for i in numbers:
        print(i)


if __name__ == '__main__':
    main()

