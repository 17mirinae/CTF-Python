N = int(input())
L = list(map(int, input().split()))
cnt = N

for i in range(N):
    if L[i] > 2:
        # 2~n-1까지의 값으로 나누어지면 제외
        tmp = [j for j in range(2,L[i])]
        for k in tmp:
            if L[i] % k == 0:
                cnt -= 1
                break
    # 2인 경우는 나눌 사이 값이 없음
    elif L[i] == 2:
        continue
    # 1 이하의 값의 경우
    else:
        cnt -= 1
        
print(cnt)
