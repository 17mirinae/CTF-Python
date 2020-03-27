# M ~ N 사이의 소수 찾기
M = int(input())
N = int(input())
result = []
if M == 1:
    M += 1
for i in range(M, N+1):
    n = 0 # 나누어 떨어지는 수의 개수
    for j in range(2, i):
        if i % j == 0:
            n += 1 
    if n == 0:
        result.append(i)
if not result: #빈 리스트는 false 값을 가짐
    print(-1)
else:
    print(sum(result))
    print(min(result))
#################### 시간초과 ####################

M = int(input())
N = int(input())
result = []
if M == 1:
    M += 1
for i in range(M, N+1):
    n = 0 # 나누어 떨어지는 수의 개수
    for j in range(2, i):
        if i % j == 0:
            n+=1
            break
    if n == 0:
        result.append(i)
if not result: #빈 리스트는 false 값을 가짐
    print(-1)
else:
    print(sum(result), "\n", min(result), sep='')

#################### 두번째 반복문이 무의미한 루프를 타지 않도록 break를 설정 ####################