#!/usr/bin/env python3
# coding: utf-8

def solve(num_list):
    num_list.sort()
    c = num_list[-1]
    if sum(list(map(lambda x: x ** 2, num_list[:2]))) == c ** 2:
        return 'right'
    else:
        return 'wrong'


def main():
    while True:
        num_list = list(map(int, input().split()))

        if num_list == [0,0,0]:
            return

        print(solve(num_list))


if __name__ == '__main__':
    main()

