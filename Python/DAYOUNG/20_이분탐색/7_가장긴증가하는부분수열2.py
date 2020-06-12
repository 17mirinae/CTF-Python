# https://claude-u.tistory.com/441

# 이진 탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다
# from bisect import bisect_left

# input()
# A = list(map(int, input().split()))
# dp = []

# for i in A:
#     # 자신이 들어갈 위치 k
#     k = bisect_left(dp, i)
#     # i가 가장 큰 숫자라면
#     if len(dp) <= k:
#         dp.append(i)
#     else:
#         #자신보다 큰 수 중 최솟값과 대체
#         dp[k] = i

# print(len(dp))

# https://suri78.tistory.com/199

import sys

def find(target):
    start, end = 1, len(stack)-1
    while start < end:
        mid = (start + end) //2
        print("mid = ", mid)
        if stack[mid] < target:
            print("stack[mid] < target", stack[mid], target)
            start = mid + 1
            print("start = ", start)
        elif stack[mid] > target:
            print("stack[mid] > target:", stack[mid], target)
            end = mid
            print("end",end)
        else:
            print("else")
            start = end = mid
            print("start, end, mid", start, end, mid)
    print("end = ", end)
    return end

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]

for a in arr:
    if stack[-1] < a:
        print("stack append = ", a)
        stack.append(a)
    else:
        print("call find(a)", a)
        stack[find(a)] = a

print(stack)
print(len(stack)-1)

# https://developmentdiary.tistory.com/355