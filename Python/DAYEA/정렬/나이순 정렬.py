N = int(input())
L = []
for i in range(N):
    tmp = input().split()
    t = (int(tmp[0]), tmp[1])
    L.append(t)

L.sort(key=lambda x: (x[0]))
    
for j in L:
    print(j[0], j[1])
