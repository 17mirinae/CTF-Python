import sys
import math

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x

    factor = math.ceil(math.sqrt(distance))

    flag1 = (factor - 1) ** 2
    flag2 = factor ** 2

    if distance >= (flag1 + flag2) / 2:
        res = factor * 2 - 1
    else:
        res = factor * 2 - 2

    result.append(res)

for i in result:
    print(i)
