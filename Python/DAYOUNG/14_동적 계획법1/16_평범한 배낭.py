#틀렸습니다.
n, k = map(int, input().split())

w_v = []
for _ in range(n):
    w, v = map(int, input().split())
    w_v.append([w,v])

# 1. 무게 2. 가치

dp = [ [0, 0] for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[0] = w_v[0]
    for j in range(i):
        if dp[j][0] + w_v[i][0] <= k:
            dp[i][0] = dp[j][0]+w_v[i][0]
            dp[i][1] = dp[j][1]+w_v[i][1]
    if not dp[i][0]:
        dp[i] = w_v[i]
    # print(dp[i])

result = 0
for i in range(n):
    if result < dp[i][1]:
        result = dp[i][1]
print(result)