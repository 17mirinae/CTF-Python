N = int(input())
L = [_ for _ in range(10**(N-1), 10**N)]
cnt = 0

if N == 1:
    cnt = 9
else:
    for l in L:
        x = 0
        tmp = str(l)
        for i in range(1, N):
            x += abs(int(tmp[i-1]) - int(tmp[i]))
        if N-1 == x:
            cnt = x

print(cnt)
