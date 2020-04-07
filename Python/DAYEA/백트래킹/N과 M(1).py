import itertools
# https://docs.python.org/2/library/itertools.html 참고

N, M = map(int, input().split())
P = itertools.permutations(range(1, N+1), M)

for i in P:
    print(' '.join(map(str, i))) 
