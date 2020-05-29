def expo(m, k):
    if k == 1:
        for i in range(N):
            for j in range(N):
                m[i][j] %= 1000
        return m
    elif k % 2 > 0:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        c = expo(m, k-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += c[i][k] * m[k][j]
                tmp[i][j] %= 1000
        return tmp
    else:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        c = expo(m, k//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += c[i][k] * c[k][j]
                tmp[i][j] %= 1000
        return tmp

N, K = map(int,input().split())
A = [list((map(int, input().split()))) for _ in range(N)]
for i in expo(A, K):
    for j in i:
        print(j, end = ' ')
    print()
