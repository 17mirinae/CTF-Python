N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(1, N+1):
    tmp = 0
    for j in range(i):
        tmp += L[j]
    ans += tmp
    
print(ans)
