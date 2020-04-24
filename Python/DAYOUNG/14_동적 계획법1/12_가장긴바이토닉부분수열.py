n = int(input())

arr = list(map(int, input().split()))

up = [1] * n
down = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            up[i] = max(up[i], up[j]+1)

for i in range(n-1, 0, -1):
    for j in range(n-1, i-1, -1):
        if arr[i] > arr[j]:
            down[i] = max(down[i], down[j]+1)

cnt = 0
for i in range(n):
    if cnt < up[i] + down[i] -1 :
        cnt = up[i] + down[i] -1
print(cnt)


#10 20 30 40 30 20 10
#up[] : 10, 20 ,30, 40
#down[] : 10, 20, 30, 40

# index = 1
up = 2
down = 2