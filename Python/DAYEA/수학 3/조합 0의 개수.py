from math import factorial
n, m = map(int, input().split())

L = str(factorial(n) // (factorial(m) * factorial(n-m)))

cnt = 0
for i in range(len(L)-1, -1, -1):
    if L[i] == '0':
        cnt += 1
    else:
        break
        
print(cnt)

#시간초과
