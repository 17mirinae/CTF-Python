n = int(input())

def fibo(N):
    if N == 0:
        return 0
    elif N ==1:
        return 1
    else:
        return fibo(N-2)+fibo(N-1)

print(fibo(n))