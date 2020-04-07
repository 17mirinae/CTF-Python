#!/usr/bin/env python3
# coding: utf-8

from itertools import combinations as cm
import math

def main():
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]

    min_ans = 123456789

    for case in cm(range(1,n+1),n//2):
        s1 = s2 = 0

        for i in case:
            for j in case:
                s1+=data[i-1][j-1]

        res = set(range(1, n + 1)) - set(case)
        for i in res:
            for j in res:
                s2 += data[i-1][j-1]

        min_ans=min([min_ans,abs(s1-s2)])

    print(min_ans)


if __name__ == '__main__':
    main()

