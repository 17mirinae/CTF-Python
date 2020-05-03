N, K = map(int, input().split())

a = b = c = 1
for i in range(1, N+1):
    a *= i
for j in range(1, K+1):
    b *= j
for k in range(1, (N-K)+1):
    c *= k
    
print(int(a/(b*c)))
