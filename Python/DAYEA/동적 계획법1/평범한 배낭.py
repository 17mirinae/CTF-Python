N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(K+1)]

for i in range(N):
    for j in range(K, 1, -1):
        if L[i][0] <= j:
            dp[j] = max(dp[j], dp[j-L[i][0]] + L[i][1])

print(dp[-1])
