import statistics
from collections import Counter
N = int(input())

L = [int(input()) for i in range(N)]
L.sort()

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
s = round(sum(L)/N, 1)
print(s)
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
m = statistics.median(L)
print(m)
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
c = Counter(L).most_common(1)
print(c[0][0])
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(L)-min(L))
