S = input()
A = 0
for i in S:
    # 입력된 문자를 아스키코드로 변경하여 범위로 계산
    tmp = ord(i)
    if tmp >= 65 and tmp <= 67:
        # 숫자 1을 걸려면 총 2초가 필요하고,  한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다. 
        A += 3
    elif tmp >= 68 and tmp <= 70:
        A += 4
    elif tmp >= 71 and tmp <= 73:
        A += 5
    elif tmp >= 74 and tmp <= 76:
        A += 6
    elif tmp >= 77 and tmp <= 79:
        A += 7
    elif tmp >= 80 and tmp <= 83:
        A += 8
    elif tmp >= 84 and tmp <= 86:
        A += 9
    elif tmp >= 87 and tmp <= 90:
        A += 10
print(A)
