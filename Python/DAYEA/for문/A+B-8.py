import sys
N= int(input())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i+1, A, B,  A+B))
