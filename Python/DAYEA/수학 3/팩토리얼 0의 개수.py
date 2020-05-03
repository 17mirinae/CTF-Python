from math import factorial
N = int(input())
L = str(factorial(N))

cnt = 0
for i in range(len(L)-1, -1, -1):
    if L[i] == '0':
        cnt += 1
    else:
        break
        
print(cnt)
