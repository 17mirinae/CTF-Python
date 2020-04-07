#https://dojinkimm.github.io/problem_solving/2019/10/16/boj-2580-sudoku.html
blank=[]
for _ in range(9):
    blank.append(list(map(int, input().split())))

# for i in range(9):
#     print(blank[i])

zero_cnt = 0
for num in blank:
    for i in range(9):
        if num[i] == 0:
            zero_cnt += 1

def zero_count(a, b):
    zero = 0
    if b == 0: #행
        for i in range(9):
            if blank[a][i] == 0:
                zero += 1
    else: #열
        for i in range(9):
            if blank[i][b] == 0:
                zero += 1
    return zero

def find_num(a, b):
    if b==0:
        return 45 - sum(blank[a])
    else:
        tmp =0
        for i in range(9):
            tmp += blank[i][b]
        return 45 -tmp

def write_line(a, b):
    if zero_count(a, b) == 1:
        find_num(a, b)

