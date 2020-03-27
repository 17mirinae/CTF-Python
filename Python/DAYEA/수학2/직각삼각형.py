while True:
    L = list(map(int, input().split()))
    L.sort()
    if sum(L) == 0:
        break
    if L[2]**2 == L[0]**2 + L[1]**2:
        print('right')
    else:
        print('wrong')
