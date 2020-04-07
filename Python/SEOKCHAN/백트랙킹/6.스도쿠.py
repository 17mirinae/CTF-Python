#!/usr/bin/env pypy3
# coding: utf-8

import sys
input = sys.stdin.readline

def get_available(x, y):
    available = [ i+1 for i in range(9) ]

    for i in range(9):
        if sudoku[x][i] in available:
            available.remove(sudoku[x][i])
        if sudoku[i][y] in available:
            available.remove(sudoku[i][y])

    x //= 3
    y //= 3
    for i in range(x * 3, (x + 1) * 3):
        for j in range(y * 3, (y + 1) * 3):
            if sudoku[i][j] in available:
                available.remove(sudoku[i][j])

    return available


def f(cnt):
    global flag, todo, sudoku

    if flag:
        return

    if cnt == len(todo):
        for s in sudoku:
            print(* s)

        flag = True
        return

    else:
        (x, y) = todo[cnt]
        available = get_available(x, y)

        for i in available:
            sudoku[x][y] = i
            f(cnt + 1)

            # 정답이 없으면 다시 검사
            sudoku[x][y] = 0



def main():
    global sudoku, todo, flag
    sudoku = [ list(map(int, input().strip().split())) for i in range(9) ]
    todo = [ (i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0 ]

    flag = False
    f(0)


if __name__ == '__main__':
    main()

