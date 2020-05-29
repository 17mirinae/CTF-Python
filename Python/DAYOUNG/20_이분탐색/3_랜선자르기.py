import sys

k, n = map(int, sys.stdin.readline().split())

line = [int(sys.stdin.readline()) for _ in range(k)]

# https://claude-u.tistory.com/443

# 이분탐색 처음과 끝 위치
start, end = 1, max(line)

#랜선을 찾는 알고리즘
while start <= end:
    mid = (start + end ) //2
    lines = 0
    for i in line:
        lines += i // mid #분할된 랜선 수
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)