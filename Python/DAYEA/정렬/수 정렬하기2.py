import sys

N = int(input())

l = [int(sys.stdin.readline()) for i in range(N)]

L = "\n".join(map(str, sorted(l)))
print(L)
