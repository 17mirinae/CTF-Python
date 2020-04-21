N = int(input())
S = list(map(int, input().split()))
up = [1]*N
down = [1]*N

for i in range(N):
    for j in range(i):
        if S[i] > S[j]:
            up[i] = max(up[i], up[j]+1)
            
for i in range(N-1, 0, -1):
    for j in range(N-1, i-1, -1):
        if S[i] > S[j]:
            down[i] = max(down[i], down[j]+1)
            
cnt = 0
for i in range(N):
    if cnt < up[i] + down[i] - 1:
        cnt = up[i] + down[i] - 1
        
print(cnt)
