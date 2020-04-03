N = int(input())
L = []
for i in range(N):
    tmp = input()
    t = (tmp, len(tmp))
    if t in L:
        pass
    else:
        L.append(t)

L.sort(key=lambda x: (x[1], x[0]))
    
for j in L:
    print(j[0])
