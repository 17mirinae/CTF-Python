N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
L = sorted(L, key = lambda x: (x[1], x[0]))

end = cnt = 0
for s, e in L:
    if s >= end:
        cnt += 1
        end = e
        
print(cnt)
