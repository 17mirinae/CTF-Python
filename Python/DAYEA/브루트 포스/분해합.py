N = int(input())

ans = 0
for i in range(1, N+1):
    I = str(i)
    tmp = 0
    for j in I:
        tmp += int(j)
    if N == (i + tmp):
        ans = i
        break
        
print(ans)
