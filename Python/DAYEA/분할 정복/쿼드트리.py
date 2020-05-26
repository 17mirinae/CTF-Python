import sys
N = int(sys.stdin.readline())
video = [list(sys.stdin.readline().strip()) for _ in range(N)] #x행 y열
 
def decompose(x, y, n):
    if n == 1:
        print(video[x][y], end="")
        return
  
    flag = True
    for i in range(x, x+n):
        if not flag:
            break
        for j in range(y, y+n):
            if video[i][j] != video[x][y]:
                flag = False
                break

    if flag:
        print(video[x][y], end="")
    else:
        n = n//2

        print("(", end="")
        decompose(x, y, n)
        decompose(x, y+n, n)
        decompose(x+n, y, n)
        decompose(x+n, y+n, n)
        print(")", end="")

decompose(0,0,N)
