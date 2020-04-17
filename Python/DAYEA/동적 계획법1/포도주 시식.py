N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [0] * N

if N == 1:
    dp[0] = wine[0]
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]

for i in range(2, N):
    dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])

print(dp[N-1])
