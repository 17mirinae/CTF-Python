A = input().split('-')
num = []
for a in A:
    cnt = 0
    B = a.split('+')
    for b in B:
        cnt += int(b)
    num.append(cnt)
    
ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
    
print(ans)
