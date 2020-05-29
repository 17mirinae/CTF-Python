K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]

mn, mx = 1, max(L)
while mn <= mx:
    md = (mn + mx) // 2
    n = sum([(i // md) for i in L])
    if n >= N:
        result = md
        mn = md + 1
    else:
        mx = md - 1
        
print(result)
