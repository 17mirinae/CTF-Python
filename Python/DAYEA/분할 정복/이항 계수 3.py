N, K = map(int, input().split())
P = 1000000007
def square(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 > 0:
        return square(a, b-1) * a
    else:
        d = square(a, b // 2)
        d %= P
        return d ** 2 % P
# 페르마의 소정리는 p가 소수이고 a가 정수이면 a^(p-1) % p = 1
# (n!/(k!(n-k)!)) % p = (A / B) % p
# (A * B^-1) % p --> (A % p) * (B^-1 % p)
# (A % p) * (B^(p-2) % p) --> (A * (B^(p-2))) %p
A = 1
B = 1
for i in range(1,N+1):
    A *= i
    A %= P
for i in range(1, K+1):
    B *= i
    B %= P
for i in range(1, N-K+1):
    B *= i
    B %= P
    
B = square(B,(P-2) % P)
print((A * B) % P) 
