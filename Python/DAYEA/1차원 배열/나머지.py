# 10줄의 입력을 받아 하나의 변수에 저장하여, 배열 형태로 저장됨
num =[int(input()) for i in range(10)]
N=0
for i in range(10):
    # 각 수의 42에 대한 나머지 저장
    num[i] = num[i]%42
for a in range(42):
    # 0~41까지의 수가 나머지가 될 수 있는 수 
    if a in num:
        # 만약 그 수가 이 배열 안에 있다면 1을 더한다. (배열에 대해서가 아닌 0~41까지의 수에 대해서이므로 중복이 발생하지 )
        N += 1
print(N)
