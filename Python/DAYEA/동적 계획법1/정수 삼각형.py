N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(L[i])):
        if j == 0:    # 열의 첫칸일 경우, 자신의 우측 윗칸을 더해준다.
            L[i][j] += L[i - 1][j]
        elif i == j:    # 열의 마지막 칸의 경우, 자신의 좌측 윗칸을 더해준다.
            L[i][j] += L[i - 1][j - 1]
        else:    # 일반적인 경우, 자신의 인접한 윗칸 두개 중 큰 것을 자신에게 더한다.
            L[i][j] += max(L[i - 1][j - 1], L[i - 1][j])
            
print(max(L[N - 1]))    # 마지막 열의 가장 큰 수을 출력
