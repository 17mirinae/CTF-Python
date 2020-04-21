N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

L = sorted(L, key = lambda x: x[0])
dp = [1] + [0]*(N-1)

for i in range(1, N):
    minimum = 0
    for j in range(i):
        if L[i][1] > L[j][1]:
            minimum = max(dp[j], minimum)
    dp[i] = minimum + 1
    
print(N - max(dp))
