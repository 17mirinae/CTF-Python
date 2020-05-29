# https://claude-u.tistory.com/441

# 이진 탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다
from bisect import bisect_left

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    # 자신이 들어갈 위치 k
    k = bisect_left(dp, i)
    # i가 가장 큰 숫자라면
    if len(dp) <= k:
        dp.append(i)
    else:
        #자신보다 큰 수 중 최솟값과 대체
        dp[k] = i

print(len(dp))
