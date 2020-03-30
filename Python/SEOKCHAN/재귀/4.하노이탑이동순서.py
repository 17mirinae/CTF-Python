#!/usr/bin/env python3
# coding: utf-8

log_msg = ''

def logger(src, dst):
    print('{0} {1}'.format(src, dst))


def get_total_move(n):
    t = 0
    for i in range(n):
        t *= 2
        t += 1
    return t


def solve(n, src, via, dst):
    if n == 1:
        logger(src, dst)
        return

    solve(n - 1, src, dst, via)
    logger(src, dst)
    solve(n - 1, via, src, dst)


def main():
    n = int(input())
    print(get_total_move(n))
    solve(n, 1, 2, 3)


if __name__ == '__main__':
    main()

