#틀렸음(예제2)
# n = int(input())

# number = []
# for _ in range(n):
#     num = int(input())
#     if number and num == 0:
#         number.pop()
#         number.append(0)
#     else:
#         number.append(num)

# print(sum(number))

n = int(input())
stack = []

for _ in range(n):
    num = int(input())
    if num == 0:
        #del : 지우고자 하는 리스트의 인덱스를 받아서 지우는 방식, 지워진 인덱스 값을 반환하지 않는다(pop과 다른점)
        del stack[-1] 
    else:
        stack.append(num)
if not stack:
    print(0)
else:
    print(sum(stack))