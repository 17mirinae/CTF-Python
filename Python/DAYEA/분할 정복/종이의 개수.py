import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0] * 3 # -1, 0, 1
   
def check(x, y, n):
    temp = paper[x][y]
    for i in range(n):
        for j in range(n):
            if temp != paper[x + i][y + j]:
                return False
    return True

def divide(x, y, n):
    if check(x, y, n):
        result[paper[x][y] + 1] += 1
    else:
        n = n // 3
        for i in range(3):
            for j in range(3):
                divide(x + i*n, y + j*n, n)
    return

divide(0, 0, N)
for i in range(3):
    print(result[i])
