import math

def prime(x):
    y = int(math.sqrt(x))+1
    if x == 1:
        return False
    for i in range(2, y):
       if x % i == 0:
            return False
    return True

M, N = map(int, input().split())
for j in range(M, N+1):
    if prime(j) == True:
        print(j)
