from itertools import product

N, M = map(int, input().split())
p = product(range(1, N+1), repeat=M)

for i in sorted(p):
    print(' '.join(map(str, i)))