N = int(input())
L = []
for i in range(N):
    l = list(map(int, input().split()))
    L.append(l)
    
L.sort(key=lambda x: (x[0], x[1]))
for j in L:
    print(j[0], j[1])
