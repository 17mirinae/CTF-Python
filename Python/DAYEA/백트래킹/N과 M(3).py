import itertools

N, M = map(int, input().split())
p = itertools.product(range(1, N+1), repeat=M)

for i in p:
    print(' '.join(map(str, i))) 
