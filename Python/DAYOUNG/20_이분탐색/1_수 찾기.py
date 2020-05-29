# https://www.acmicpc.net/step/29

# 시간초과
# import sys

# n = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# B = list(map(int, sys.stdin.readline().split()))

# for i in B:
#     result = 0
#     for j in A:
#         if i == j:
#             result = 1
#             del A[A.index(j)]
#             break
#     print(result)

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort() #이진탐색을 위해서 A만 정렬

m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) //2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for k in range(m):
    print(binary_search(A, B[k]))
