def promising(y):    # 퀸의 위치가 서로 공격이 불가능한 위치인지 확인
    for i in range(y):
        # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
        if row[i] == row[y] or abs(row[i]-row[y]) == abs(i-y):
            return False
    return True
 
def N_queen(n):
    # 재귀호출 시에도 값을 유지하면 더해져야하므로 global로 선언 
    global result
    if n == N:    # 마지막 열에 도착했을 시
        result += 1
    else:
        for i in range(N):
            row[n] = i    # 가능한 퀸의 위치를 0~N까지 확인
            if promising(n):    # 서로 공격이 불가능한 위치라면
                N_queen(n+1)    # 다음 열로 이동하여 reculsive하게 확인
 
 
N = int(input())
row = [0]*15
result = 0
N_queen(0)
print(result)
