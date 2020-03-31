N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(input())

cnt = 0
for i in range(M):
    if 'BB' in L[i] or 'WW' in L[i]:
        cnt += 1

print(cnt)
