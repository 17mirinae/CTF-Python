#!/usr/bin/env python3
# coding: utf-8

def get_roomname(h, w):
    # h = 층, w = 방번호
    return str(h) + str(w).zfill(2)


def solve(h, w, n):
    # h = 층수, w = 방 수, n = 손님 번호
    if n % h == 0:
        floor = h
    else:
        floor = n % h
    return get_roomname(floor, (n - 1) // h + 1)


def main():
    for _ in range(int(input())):
        h, w, n = map(int, input().split())
        print(solve(h, w, n))


if __name__ == '__main__':
    main()

