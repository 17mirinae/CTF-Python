#!/usr/bin/env python3
# coding: utf-8

def f(cnt, n, m):
    global res, visited

    if cnt == m:
        print(*res)
        return

    else:
        for i in range(n):

            # visited를 이용해서 중복되는 숫자가 없도록 함.
            if visited[i] == 0:
                visited[:i] = [1] * len(visited[:i])
                # visited[i] = 1

                res[cnt] = (i + 1)

                f(cnt + 1, n, m)
                visited[:i] = [0] * len(visited[:i])


def main():
    global res, visited

    n, m = map(int, input().split())

    # Setting.
    res = [0] * m
    visited = [0] * n

    f(0, n, m)


if __name__ == '__main__':
    main()

