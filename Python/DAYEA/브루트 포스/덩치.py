N = int(input())

X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for j in range(N):
    cnt = 1
    for k in range(N):
        if X[j] < X[k] and Y[j] < Y[k]:
            cnt += 1
    print(cnt, end=" ")
