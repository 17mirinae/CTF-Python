L = []
while True:
    tmp = list(map(int, input().split()))
    if tmp == [0, 0]:  
        break
    else:
        L.append(tmp)
        
for a, b in L:
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
