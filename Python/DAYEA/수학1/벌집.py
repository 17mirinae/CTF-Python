N = int(input())
A = 1
C = 1
tmp = 1

# N이 있는 범위가 나올 때까지 무한 루프
while True:
    # 1일 경우는 따로 처리
    if N == 1:
        break
    # N의 범위 찾기
    elif A+1 <= N <= A+tmp*6:
        C = tmp+1
        break
    # 범위 구하기
    else:
        A += tmp*6
        tmp += 1

print(C)
