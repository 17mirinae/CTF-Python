import sys

# 가로 체크
def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True

# 세로 체크
def vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True

# 3x3 subgrid 체크
def subgrid(x, y, val):
    nx = x//3 * 3    # 몇번째 상자인지 확인
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+j]:
                return False
    return True

def backtracking(index):    # zeros배열의 인덱스
    if index == len(zeros):
        for row in sudoku:
            print(*row)
        sys.exit(0) # 함수 종료
    else:
        for i in range(1, 10):
            nx = zeros[index][0]    # 0이 있는 x좌표
            ny = zeros[index][1]    # 0이 있는 y좌표

            # 세로, 가로, 3x3에 내가 대체하려고하는 숫자가 존재하지 않는다면
            if horizontal(nx, i) and vertical(ny, i) and subgrid(nx, ny, i):
                sudoku[nx][ny] = i    # i를 넣고 확인
                backtracking(index+1)    # 칸이 다 채워지도록 reculsive
                sudoku[nx][ny] = 0    # 정답이 없는 경우를 대비하여 0으로 초기화


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# (행, 열)형태로 0이 있는 배열의 좌표를 담은 배열 (0이 담긴 좌표만 확인하도록)
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
backtracking(0)
