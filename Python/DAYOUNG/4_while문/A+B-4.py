import sys

for string in sys.stdin:
    a, b = map(int, string.split())
    print(a+b)