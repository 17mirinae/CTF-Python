N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[0] = stair[0]
        continue
    elif i == 1:
        dp[1] = stair[0] + stair[1]
        continue
    elif i == 2:
        # max(시작 위치 + 1칸 + 2칸의 경우, 2칸 + 한칸의 경우)
        dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
        continue
    dp[i] = max(stair[i] + stair[i - 1] + dp[i - 3],  stair[i] + dp[i - 2])

print(dp[N-1])
