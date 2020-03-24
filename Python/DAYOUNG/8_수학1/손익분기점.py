#A만원 고정비용
#B만원 한 대의 노트북을 생산하는데 드는 가변비용
#C만원 노트북 가격

# A, B, C = map(int, input().split())

# n = 1

# while 1:
#     break_point = A + B*n
#     if C*n > break_point:
#         print(n)
#         break
#     else:
#         n += 1
######################## 시간초과 & 손익분기점 존재하지 않을 때 구현X ######################
# A, B, C = map(int, input().split())

# n = 1

# while C*n <= A+B*n:
#     n += 1
# print(n)
######################## 시간초과 & 손익분기점 존재하지 않을 때 구현X ######################
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(int(A//(C-B)+1))

#https://wlstyql.tistory.com/51
# 이익 = (1대 당 가격 C - 1대 당 생산비 B) * k 대 - 고정 비용 A
# E = (C - B) * k - A
# 손익분기점 : E = 0 일때