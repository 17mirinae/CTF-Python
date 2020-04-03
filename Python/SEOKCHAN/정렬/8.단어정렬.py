#!/usr/bin/env python3
# coding: utf-8

import sys

def main():
    input = sys.stdin.readline
    words = [input().strip() for _ in range(int(input().strip()))]
    words = list(set(words))
    words.sort(key=lambda x: (len(x), x))

    for w in words:
        print(w)


if __name__ == '__main__':
    main()

