#!/usr/bin/env python3
# coding: utf-8

def solve(n, cards):

    items = []

    for i in range(len(cards)):
        for j in range(len(cards)):
            for k in range(len(cards)):
                if any([i == j, j == k, k == i]):
                    continue

                sum_res = sum([cards[i], cards[j], cards[k]])
                if sum_res <= n:
                    items.append(sum_res)

    return max(items)


def main():
    _, n = map(int, input().split())
    cards = list(map(int, input().split()))
    print(solve(n, cards))


if __name__ == '__main__':
    main()

