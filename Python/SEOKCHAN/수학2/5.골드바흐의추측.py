#!/usr/bin/env python3
# coding: utf-8

num_list = [True] * 10001
num_list[0] = num_list[1] = False


def solve(n):
    global num_list
    for i in range(2, n + 1):
        if num_list[i] is not True:
            continue

        num_list[i*2::i] = [False] * (10000 // i - 1)

    # 골드바흐의 수를 만족하는 쌍을 구하는 코드
    i = n // 2
    while True:
        if num_list[i] is True and num_list[n - i] is True:
            result = (i, n - i)
            break
        i -= 1

    return result


def main():
    for _ in range(int(input())):
        n = int(input())
        x, y = solve(n)
        print(x, y)


if __name__ == '__main__':
    main()

