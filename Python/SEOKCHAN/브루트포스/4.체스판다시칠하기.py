#!/usr/bin/env python3
# coding: utf-8

def set_plate():
    n, m = map(int, input().split())
    plate = []
    for i in range(n):
        row = list(input())
        plate.append(row)
    return n, m, plate


def get_repaint(plate):
    result = []
    row = [ ['W', 'B'] * 4, ['B', 'W'] * 4 ]
    for i in range(2):
        repaint = 0
        for j in range(8):
            check = row[(i + j) % 2]
            for k in range(8):
                if plate[j][k] != check[k]:
                    repaint += 1
        result.append(repaint)

    return min(result)


def solve(n, m, plate):
    result = []
    i = j = 0
    while i <= n - 8:
        j = 0
        while j <= m - 8:
            tmp_plate = [ list(plate[i+k][j:j+8]) for k in range(8) ]
            res = get_repaint(tmp_plate)
            result.append(res)

            j += 1
        i += 1

    return min(result)


def main():
    n, m, plate = set_plate()
    print(solve(n, m, plate))


if __name__ == '__main__':
    main()

