# 행렬의 곱
# A: n * m 크기
# B: m * k 크기
import sys

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m, k = map(int, sys.stdin.readline().split())

b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for i in range(n):
    for j in range(k):
        tmp = 0
        for l in range(m):
            tmp += a[i][l] * b[l][j]
        sys.stdout.write(str(tmp)+ " ")
    sys.stdout.write("\n")
