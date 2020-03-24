#!/usr/bin/env python3
# coding: utf-8

def get_people(k, n):
    # 0층 세팅
    people = [[i for i in range(1, 15)]]

    # 1층부터 세팅
    for i in range(1, 15):
        people.append([])
        # 1호부터 14호까지
        for j in range(1, 15):
            people[i].append(sum(people[i - 1][:j]))
    return people[k][n-1]


def solve(k, n):
    # k = 층, n = 호
    return get_people(k, n)


def main():
    for _ in range(int(input())):
        k = int(input())
        n = int(input())
        print(solve(k, n))


if __name__ == '__main__':
    main()

