P = [1, 1, 1, 2, 2, 3, 4] + [0]*93
for i in range(7,100):
    P[i] = P[i-2] + P[i-3]

N = int(input())
L = [int(input()) for _ in range(N)]
for l in L:
    print(P[l-1])
