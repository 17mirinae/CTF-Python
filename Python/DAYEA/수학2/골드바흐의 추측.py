import sys

L = [1] * (10001)
L[0] = 0
L[1] = 0
for i in range(2, 101):
    if L[i] == 1:
        for j in range(i+i, 10001, i):
            L[j] = 0

prime = []
for k in range(10001):
    if L[k] == 1:
        prime.append(k)
        
T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    for l in range(int(n/2), 1, -1):
        if L[l] + L[n-l] == 2:
            print(l, n-l)
            break
