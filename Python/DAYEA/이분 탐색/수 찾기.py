import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

D = {}
for a in A:
    D[a] = 1
for b in B:
    try:
        print(D[b])
    except:
        print(0)
