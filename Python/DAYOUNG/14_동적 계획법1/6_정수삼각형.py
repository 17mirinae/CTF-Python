import math
n = int(input())

triagle = []

for i in range(n):
    triagle.append(list(map(int, input().split())))

#점화식
#dp[i] = max(dp[i][j-1], dp[i][j]) + arr[i][j]

for i in range(1, n):
    for k in range(len(triagle[i])):
        #인덱스 0
        if k == 0:
            triagle[i][k] += triagle[i-1][k]
        #마지막 인덱스
        elif k == len(triagle[i])-1:
            triagle[i][k] += triagle[i-1][k-1]
        #그 외
        else:
            triagle[i][k] += max(triagle[i-1][k-1], triagle[i-1][k])

#마지막 층의 최대 값 출력
print(max(triagle[n-1]))
