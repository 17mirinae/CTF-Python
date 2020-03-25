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
    res = sum(primes)

    if res == 0:
        return -1, 0
    else:
        min_prime = min(primes)
        return (res, min_prime)


def main():
    m = int(input())
    n = int(input())
    res, min_prime = solve(m, n)
    if res == -1:
        print(-1)
    else:
        print(res)
        print(min_prime)


if __name__ == '__main__':
    main()

