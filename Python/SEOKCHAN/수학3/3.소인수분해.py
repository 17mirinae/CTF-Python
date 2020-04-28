#!/usr/bin/env python3
# coding: utf-8

def solve(n):
    # n보다 작은 소수 구하기
    nums = [True] * (n + 1)
    nums[0] = nums[1] = False
    for i in range(2, n + 1):
        if nums[i] is False:
            continue
        elif n % i == 0:
            for j in range(2, (n // i) + 1):
                nums[i * j] = False

    # n 자체가 소수인 경우
    if nums[n] is True:
        return [n]

    else:
        factors = []
        primes = [i for i in range(2, n + 1) if nums[i] is True]
        while True:
            if n == 1:
                break

            for p in primes:
                if n % p == 0:
                    factors.append(p)
                    n = n // p
                    break

        return factors


def main():
    n = int(input())
    factors = solve(n)
    print(*factors, sep='\n')


if __name__ == '__main__':
    main()

