import sys

# 나무의 수 n, 최소 m미터의 나무
n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, input().split()))

start, end = 1, max(tree)

#https://claude-u.tistory.com/446
while start <= end:
    meter = 0
    mid = (start + end) //2
    for i in tree:
        if i >= mid:
            meter += i - mid
    if meter >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)