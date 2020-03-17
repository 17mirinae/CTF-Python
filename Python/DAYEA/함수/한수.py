def arith(n):
    # 100보다 작으면 자기자신이 한수
    if n<100:
        result = True
    else:
        n = list(str(n))
        sub = int(n[1])-int(n[0])
        for i in range(1, len(n)-1):
            if sub == (int(n[i+1])-int(n[i])):
                result = True
            else:
                # 한수가 아님
                result = False
                break
    return result

N = int(input())
cnt = 0
for i in range(1, N+1):
    # boolen타입을 int타입과 연산하면, True일 경우는 1이고 False일 경우는 0이다.
    cnt += arith(i)
print(cnt)
