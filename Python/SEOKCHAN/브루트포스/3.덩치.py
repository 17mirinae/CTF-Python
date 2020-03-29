#!/usr/bin/env python3
# coding: utf-8

def is_bigger(p1, p2):
    if p1[0] > p2[0] and p1[1] > p2[1]:
        return True
    return False


def solve(people):
    len_people = len(people)
    result = [1] * len_people
    for i in range(len_people):
        for j in range(len_people):
            if i == j:
                continue

            if is_bigger(people[j], people[i]):
                result[i] += 1

    return ' '.join([str(r) for r in result])



def main():
    people = []

    for _ in range(int(input())):
        (w, h) = map(int, input().split())
        people.append((w, h))

    print(solve(people))


if __name__ == '__main__':
    main()

