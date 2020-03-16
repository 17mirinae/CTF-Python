#!/usr/bin/env python3

max = 10000
num_list = [ True for i in range(1, 100000) ]


def d(num):
    return num + sum(map(int, list(str(num))))


def calc(num):
    tmp = 0
    while num <= max:
        if tmp == d(num):
            return
        tmp = d(num)
        if tmp > max:
            return
        try:
            num_list[tmp] = False
        except:
            pass


def main():
    for i in range(1, max + 1):
        calc(i)

    print('\n'.join([str(i) for i in range(1, max + 1) if num_list[i] is True]))



if __name__ == '__main__':
    main()


