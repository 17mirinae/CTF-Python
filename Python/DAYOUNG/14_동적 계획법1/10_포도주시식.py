#https://claude-u.tistory.com/204

import sys

n = int(sys.stdin.readline())
wine = [0]
result = [0 for _ in range(wine+1)]
for _ in range(n):
    wine.append(int(input()))

for i in range(1, wine+1):
    if i == 1:
        result[1] = wine[1]
    elif i == 2:
        result[2] = wine[1] + wine[2]
    else:
        result[i] = max(result[i-3] + wine[i-1] + wine[i], result[i-2]+wine[i], result[i-1])

print(result[i])