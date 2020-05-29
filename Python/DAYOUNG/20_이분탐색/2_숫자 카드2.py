# 시간초과 조팔
# import sys

# n = int(sys.stdin.readline())
# N = list(map(int, sys.stdin.readline().split()))
# N.sort()

# m = int(sys.stdin.readline())
# M = list(map(int, sys.stdin.readline().split()))

# def binary_search(a, x):
#     start = 0
#     end = len(a) - 1
#     while start <= end:
#         mid = (start + end) //2
#         if x == a[mid]:
#             if a[mid+1] == x or a[mid-1] == x:
#                 return checkup(start, end, a, x)
#             else:
#                 return 1
#         elif x > a[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0

# def checkup(start, end, a, x):
#     cnt = 0
#     for i in range(start, end+1):
#         if a[i] == x:
#             cnt += 1
#     return cnt

# for i in range(m):
#     print(binary_search(N, M[i]), end=" ")


# https://chancoding.tistory.com/45
# 다양한 방식으로 풀이함
from sys import stdin
_ = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
_ = stdin.readline()
M = list(map(int, stdin.readline().split()))
index, m_dic = 0, {}

for m in sorted(M):
    cnt = 0
    if m not in m_dic:
        while index < len(N):
            if m == N[index]:
                cnt += 1
                index += 1
            elif m > N[index]:
                index += 1
            else:
                break
        m_dic[m] = cnt

print(' '.join(str(m_dic[m])) for m in M)