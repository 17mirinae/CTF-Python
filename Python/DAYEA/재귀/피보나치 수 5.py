def fibonacci(n):
    if n == 0:
        ret = 0
    elif n == 1:
        ret = 1
    else:
        ret = fibonacci(n-1) + fibonacci(n-2)
    return ret
        
N = int(input())
print(fibonacci(N))
