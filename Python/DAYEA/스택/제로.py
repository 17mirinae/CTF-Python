K = int(input())
L = []
for _ in range(K):
    i = int(input())
    if i != 0:
        L.append(i)
    else:
        L.pop()
print(sum(L))
