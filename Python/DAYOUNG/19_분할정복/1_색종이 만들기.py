#https://www.acmicpc.net/step/20

# 1회 분할
# 1사분면 : x - 0~n/2, y - 0~n/2
# 2사분면 : x - n/2~n, y - 0~n/2
# 3사분면 : x - 0~n/2, y - 0~n/2
# 4사분면 : x - n/2~n, y - n/2~n

# 2회 분할
# 1사분면 : x - 0~n/2, y - 0~n/2
    # 1 : x - 0~n/4, y - 0~n/4
    # 2 : x - n/4~n/2, y - 0~n/4
# 2사분면 : x - n/2~n, y - 0~n/2
# 3사분면 : x - n/2~n, y - 0~n/2
# 4사분면 : x - n/2~n, y - n/2~n

# https://claude-u.tistory.com/268

def quad_tree(x,y,n):
    global matrix, blue, white
    color = matrix[y][x] 
    double_break = False

    for i in range(x, x+n): #x 범위 이해안감 왜 x+n?
        if double_break:
            break
        for j in range(y, y+n):
            if matrix[j][i] != color: #이거 검사하는거 왜그러는지 이해안감, 마지막 색 검사 안한다는거야 뭐야 뭔소리야
                quad_tree(x+n//2, y, n//2) #1사분면
                quad_tree(x, y, n//2) #2사분면
                quad_tree(x, y+n//2, n//2) #3사분면
                quad_tree(x+n//2, y+n//2, n//2) #4사분면
                double_break = True
                break
    if not double_break:
        if matrix[y][x] == 1: #파란색이라면
            blue += 1
        else:
            white += 1
N = int(input())
matrix = []
blue = 0
white = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))

quad_tree(0,0,N)
print(white)
print(blue)