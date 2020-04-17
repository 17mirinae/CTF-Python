############뭐라는 거야#############

import sys

n = int(sys.stdin.readline())

def solve(stair, n):
    dp = []
    dp.append(stair[0])
    for i in range(1, n//2):
        if i == 1:
            dp.append(max(dp[i-1] + stair[i], stair[i]))
            continue
        dp.append(max(dp[i-2] + stair[i], stair[i-1]+stair[i]))
    
    for i in range(n//2, n):
        #i번째 계단으로 올라오기 위해 max(직전 계단을 밟은 경우, 직전 계단을 밟지 않은 경우)
        dp.append(max(stair[i] + stair[i-1] + dp[i-3], stair[i]+stair[i-2]))
    #print(dp)
    print(dp[-1])

stair = []
for i in range(n):
    stair.append(int(input()))

solve(stair, n)

#https://daimhada.tistory.com/181

# import sys
# N = int(sys.stdin.readline())
# stairs = list()
# for i in range(N):
#     stairs.append(int(sys.stdin.readline()))
    
# score = list()
# score.append(stairs[0])
# score.append(stairs[1]+stairs[0])
# score.append(max(stairs[1]+stairs[2],stairs[0]+stairs[2]))
 
# for i in range(3,N):
#     score.append(max(stairs[i]+score[i-2], stairs[i]+stairs[i-1]+score[i-3]))
# print(score[N-1])