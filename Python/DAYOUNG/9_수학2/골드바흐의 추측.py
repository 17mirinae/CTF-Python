import sys
import math
from itertools import product
#combinations은 중복허용X

def find_prime(n):
    limit = n
    eratos = [1] * (2 * limit + 1)
    eratos[0] = 0
    eratos[1] = 0

    for i in range(2, int(math.sqrt(len(eratos)))):
        if eratos[i]:
            for j in range(i + i, len(eratos), i):
                eratos[j] = 0
    return eratos

for T in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    tmp = []
    eratos = find_prime(n)
    for i in range(n):
        if eratos[i] == 1:
            tmp.append(i)
    combi = list(product(tmp, repeat=2))
    result = []
    for i in range(0, len(combi)):
        if sum(combi[i]) == n and combi[i][0] <= combi[i][1]:
            result.append(combi[i])
    print("%d %d" %(result[len(result)-1][0],result[len(result)-1][1]))
#시간초과