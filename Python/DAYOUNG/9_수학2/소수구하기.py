M, N = map(int, input().split())
for num in range(M, N+1):
    n = 0
    for j in range(2, num):
        if num % j == 0:
            n+=1
            break
    if n == 0:
        print(num)

############### 지겹다 시간 초과... ###############
