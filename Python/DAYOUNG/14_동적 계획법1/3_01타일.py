def tile01(n):
    answer = 0
    tmp1 = 1
    tmp2 = 2
    for i in range(1, n+1):
        if i == 1:
            answer = tmp1
        elif i == 2:
            answer = tmp2
        else:
            answer = tmp1 + tmp2
            tmp1 = tmp2 %15746
            tmp2 = answer %15746
    print(answer %15746)
tile01(int(input()))