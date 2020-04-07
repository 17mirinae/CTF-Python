#!/usr/bin/env pypy3
# coding: utf-8

def get_puttable(x, y, plate):
    pass

def path(cnt, n):
    global solution, board

    if cnt == n:
        solution += 1
        return

    # 가로
    for i in range(n):

        # ko == True면 퀸이 배치될 수 있음
        ko = True
        # 세로
        for j in range(cnt):
            if board[j] == i or abs(cnt - j) == abs(i - board[j]):
                ko = False
                break

        if ko is True:
            board[cnt] = i
            path(cnt + 1, n)


def main():
    global solution, board
    n = int(input())
    solution = 0
    board = [0] * n
    path(0, n)
    print(solution)


if __name__ == '__main__':
    main()

