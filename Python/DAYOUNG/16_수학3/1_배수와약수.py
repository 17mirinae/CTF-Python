import sys

while 1:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0:
        break

    if m%n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    else:
        print("neither")