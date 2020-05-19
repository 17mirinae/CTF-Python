#시간초과
import sys
a, b, c = map(int, sys.stdin.readline().split())

result = 1
if b == 0:
    print(result)
else:
    for _ in range(b):
        result = result * a % c
    print(result)