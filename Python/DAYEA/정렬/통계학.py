import sys
import statistics
from collections import Counter
N = int(input())

L = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
s = round(sum(L)/N)
print(s)

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
m = statistics.median(L)
print(m)

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
if len(L) == 1:
    print(L[0])
else:
    c = Counter(L)
    tmp = c.most_common()
    tmp = sorted(tmp, key = lambda x : (x[1], x[0]))
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
    
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(L)-min(L))
