N, M = map(int, input().split())
matrix = []
cnt = 0
start_B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
start_W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

for _ in range(N) :
    matrix.append(list(input()))

if matrix[0][0] == 'W' :
    for x in range(N) :
        if x%2 == 0 and matrix[x] != start_W :
            for y in range(M) :
                if matrix[x][y] != start_W[y] :
                    cnt += 1
        elif x%2 == 1 and matrix[x] != start_B
else : # 시작이 'B'라면
    for x in range(N) :
        if matrix[x] != start_B :
            for y in range(M) :
                if matrix[x][y] != start_B[W] :
                    cnt += 1

print(cnt)
