def decimal(x):
    ret = True
    if x > 2:
        # 2~n-1까지의 값으로 나누어지면 제외
        tmp = [i for i in range(2,x)]
        for j in tmp:
            if x % j == 0:
                ret = False
    # 2인 경우는 나눌 사이 값이 없음
    elif x == 2:
        ret = True
    # 1 이하의 값의 경우
    else:
        ret = False
    return ret

M = int(input())
N = int(input())
dec = []
L = [k for k in range(M,N+1)]

for l in L:
    if decimal(l) == True:
        dec.append(l)
        
if len(dec) > 0:    
    print(sum(dec))
    print(min(dec))
else:
    print(-1)
