X = int(input())

line = 0
line_sum = 0
while X > line_sum:
    line += 1
    line_sum += line
# print(line, X, line_sum)
###몇 번째 줄에 속하는지

line_unit = 0 
m = line_sum - line
if m > X:
    line_unit = m - X - 1 # -1: 인덱스를 0부터 시작하려고
else:
    line_unit = X - m - 1 
###해당 줄의 몇번째 요소인지

if line % 2 == 0:
    A = line_unit + 1 #분자: 오름차순
    B = line - line_unit #분모: 내림차순
else:
    A = line - line_unit
    B = line_unit + 1
###입력값 번째의 분모, 분자 구하기

print(A, '/', B, sep='')

# X = int(input())

# line = 1

# #대각선으로 각 줄을 나눠 입력받은 X가 몇 번째 줄의 숫자인지 구하기
# while X > line:
#     X-=line
#     line+=1

# # 짝수 번째 줄인지, 홀수 번째 줄인지에 따라 분모, 분자 숫자의 방향이 다름
# if line % 2 == 0: #짝수인 경우 분자는 오름차순, 분모는 내림차순
#     a = X
#     b = line - X + 1
# else: #홀수인 경우 분자는 내림차순, 분모는 오름차순
#     a = line - X + 1
#     b = X

# print(a, '/', b, sep='')
############ https://deokkk9.tistory.com/11 ################