#!/usr/bin/env python3
# coding: utf-8

max = 1000
num_list = [ True for _ in range(0, max + 1) ]
num_list[max] = False


def set_han():
    for i in range(100, max):
        (top, middle, bottom) = map(int, list(str(i)))
        if middle != (top + bottom) / 2:
            num_list[i] = False


def get_smaller_han(num):
    count = 0
    for i in range(num, 0, -1):
        if num_list[i] is True:
            count += 1
    return count


def main():
    set_han()
    num = int(input())
    print(get_smaller_han(num))


if __name__ == '__main__':
    main()

