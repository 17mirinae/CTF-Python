import itertools

N, M = map(int, input().split())
c = itertools.combinations_with_replacement(range(1, N+1), M)

for i in c:
    print(' '.join(map(str, i))) 
