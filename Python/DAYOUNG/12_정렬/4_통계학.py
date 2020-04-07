import math
N = int(input())
l = [int(input()) for _ in range(N)] # 절댓값 < 4000

#산술평균
arithmetic_mean = int(round(sum(l)/N, 0))
print(arithmetic_mean)

#중앙값
m = sorted(l)
for i in range(N-1):
    if m[i] == m[i+1]:
        m.remove(m[i])
index = len(m)//2
center_value = m[index]
print(center_value)

#최빈값
#음수도 생각해야함
dic = {}
for a in m:
    if a in dic:
         dic[a] = dic[a] + 1
    else:
        dic[a] = 1
count = []
for key, value in dic.items():
    if value == max(dic.values()):
        count.append(key)
if len(count) > 1:
    print(count[1])
else:
    print(count[0])

#범위
rrange = max(l) - min(l)
print(rrange)