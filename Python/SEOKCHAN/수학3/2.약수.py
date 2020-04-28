#!/usr/bin/env python3
# coding: utf-8

def main():
    divisor_cnt = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort()

    print(divisors[-1] * divisors[0])


if __name__ == '__main__':
    main()

