import math
for i in range(int(input())):
    l = list(map(int, input().split()))
    m = sum(l[1:])/l[0]
    num = 0
    for j in l[1:]:
        if j > m:
            num += 1
    print(str('%.3f' %round(num/l[0]*100, 3)) + '%')