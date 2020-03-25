#!/usr/bin/env python3
# coding: utf-8

def solve(m, n):
    num_list = [True for i in range(0, n + 1)]
    num_list[0] = num_list[1] = False
    for i in range(0, n + 1):
        # 이미 합성수로 판단되었으면 continue
        if num_list[i] is False:
            continue

        # 소수로 판단되었으면 소수의 배수 지우기
        j = 2
        while j * i <= n:
            num_list[i * j] = False
            j += 1

    primes = [i for i in range(m, n+1) if num_list[i] is True]
    return len(primes)


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        print(solve(n + 1, n * 2))


if __name__ == '__main__':
    main()

