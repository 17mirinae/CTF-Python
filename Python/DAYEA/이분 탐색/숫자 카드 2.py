import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

D = {}
for a in A:
    try:
        D[a] += 1
    except:
        D[a] = 1
L = []
for b in B:
    try:
        L.append(D[b])
    except:
        L.append(0)
        
print(*L)
