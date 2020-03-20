import math
n = int(input()) #시험 본 과목의 개수
l = list(map(int, input().split()))
m = max(l)

for i in range(n):
    l[i] = round(l[i]/m*100, 3)

m = sum(l)/n
print(m)