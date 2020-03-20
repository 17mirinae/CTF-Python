#!/usr/bin/env python3
# coding: utf-8


def count(text):
    croatia = {
        'č': 'c=',
        'ć': 'c-',
        'dž': 'dz=',
        'đ': 'd-',
        'lj': 'lj',
        'nj': 'nj',
        'š': 's=',
        'ž': 'z=',
    }

    for cro, alpha in croatia.items():
        text = text.replace(alpha, '_')

    return len(text)


def main():
    word = input()
    print(count(word))


if __name__ == '__main__':
    main()

