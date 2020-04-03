import sys
N = int(input())
L = [0] *10001

for _ in range(N):
    tmp = int(sys.stdin.readline())
    L[tmp] += 1
    
for l in range(len(L)):
    if L[l] != 0:
        for _ in range(L[l]):
            print(l)
