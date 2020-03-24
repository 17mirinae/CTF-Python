n = int(input())
line = 1

# 대각선 몇번째 줄인지 파익
while n > line:
    n -= line
    line += 1

# 짝수 줄인 경우 분자는 오름차순, 분모는 내림차순. 홀수 줄인 경우는 반대.
if line % 2 == 0:
    a = n
    b = line - n + 1
else:
    a = line - n + 1
    b = n
    
print("%d/%d" % (a, b))
