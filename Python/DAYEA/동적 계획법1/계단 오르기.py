N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0] * N

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
# max(시작 위치 + 1칸 + 2칸의 경우, 2칸 + 한칸의 경우)
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, N):
    # 1 : 현재 위치에서 전칸을 밟아 올라온 경우 + 전전칸을 밟은 경우의 최댓값
    # 2 : 현재 위치 + 전전칸에서 올라온 경우
    dp[i] = max(stair[i] + stair[i - 1] + dp[i - 3],  stair[i] + dp[i - 2])

print(dp[N-1])
