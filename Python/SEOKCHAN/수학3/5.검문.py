#!/usr/bin/env python3
# coding: utf-8

def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y


def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]

