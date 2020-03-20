#!/usr/bin/env python3
# coding: utf-8


def get_number(character):
    number_alpha = {
        2: 'ABC',
        3: 'DEF',
        4: 'GHI',
        5: 'JKL',
        6: 'MNO',
        7: 'PQRS',
        8: 'TUV',
        9: 'WXYZ',
    }

    for number, alpha in number_alpha.items():
        if character in alpha:
            return number


def get_time(number):
    return number + 1


def main():
    word = input()
    total = 0
    for w in word:
        total += get_time(get_number(w))
    print(total)


if __name__ == '__main__':
    main()

