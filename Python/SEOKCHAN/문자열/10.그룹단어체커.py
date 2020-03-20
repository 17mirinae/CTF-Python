#!/usr/bin/env python3
# coding: utf-8


def check_group_word(text):
    alphabets = list(set(text))
    for alpha in alphabets:
        if text.count(alpha) != 1:
            tmp = text
            while True:
                start = tmp.find(alpha)
                tmp = tmp[start+1:]
                if tmp.find(alpha) == -1:
                    break
                elif tmp.find(alpha) != 0:
                    return False
    return True


def main():
    group = 0
    for _ in range(int(input())):
        if check_group_word(input()) is True:
            group += 1
    print(group)


if __name__ == '__main__':
    main()

