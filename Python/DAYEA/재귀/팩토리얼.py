def factorial(n):
    if  n == 0:
        ret = 1
    else:
        ret = n * factorial(n-1)
    return ret

N = int(input())
print(factorial(N))
