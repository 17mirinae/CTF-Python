#https://m.post.naver.com/viewer/postView.nhn?volumeNo=26896712&memberNo=33264526

#문자열로 표현된 파이썬 코드를 실행할 때 사용 : eval()함수
#https://nan491.tistory.com/entry/Python-3-eval-함수와-exec-함수


import math
import sys
from itertools import permutations

n = int(sys.stdin.readline())

numbers = sys.stdin.readline().split() #입력된 수의 배열

operator_list = list(map(int, sys.stdin.readline().split())) #각 연산자의 개수 입력됨
operators = {0:"+", 1:"-", 2:"*", 3:"/"}
operator_candidate = [] 

#각 operator의 개수를 센다. permutation으로 경우의 수를 뽑을 때 활용
for i in range(4):
    if operator_list[i] != 0:
        for _ in range(operator_list[i]):
            operator_candidate.append(operators[i])
            #각 연산자의 개수만큰ㅁ operation_candidate 배열에 operation이 추가됨

#permutation으로 경우의 수 구하기. 중복 제거를 위해 set 자료구조 사용
#set 자료구조 설명 : https://shoark7.github.io/programming/python/four-basic-datastructures-in-python
#set은 원소의 중복을 허용하지 않음 & 인덱싱 불가능(집합으로 모아놓는 형태)
candidate = set(permutations(operator_candidate, len(numbers)-1))

#inf 설명 : https://shydev.tistory.com/8
max, min = -math.inf, math.inf

for i in candidate:
    #operator가 올 수 있는 경우의 수
    i = list(i)
    stack = []
    for j in range(len(numbers)):
        stack.append(numbers[j])
        if len(stack) == 3:
            #숫자/연산자/숫자 형태로 stack에 쌓으면서 계산
            temp = int(eval("".join(stack)))
            #연산의 결과를 스택에 다시 저장
            stack = [str(temp)]
        #마지막 숫자에 도착했으면 끝
        if j == len(numbers)-1:
            break
        else:
            stack.append(i[j])
    #해당 연산자로 연산을 마친 결과
    print("stack: ", stack)
    print("stack len :", len(stack))
    answer = eval("".join(stack))
    if answer > max:
        max = answer
    if answer < min:
        min = answer
    
print(max)
print(min)

