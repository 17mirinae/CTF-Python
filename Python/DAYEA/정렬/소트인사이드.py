tmp = input()
L = []
for i in tmp:
    L.append(int(i))
    
L.sort(reverse=True)
for j in L:
    print(j, end="")
