#!/usr/bin/env python3
# coding: utf-8


def solve(points):
    x_list = list(map(lambda x: x[0], points))
    y_list = list(map(lambda x: x[1], points))

    for x in x_list:
        if x_list.count(x) == 2:
            x_list = list(set(x_list))
            x_list.remove(x)
            res_x = x_list[0]

    for y in y_list:
        if y_list.count(y) == 2:
            y_list = list(set(y_list))
            y_list.remove(y)
            res_y = y_list[0]

    return res_x, res_y


def main():
    points = []
    for _ in range(3):
        points.append(list(map(int, input().split())))
    x, y = solve(points)
    print(x, y)


if __name__ == '__main__':
    main()

