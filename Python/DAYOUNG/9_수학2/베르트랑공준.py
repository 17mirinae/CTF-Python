# while 1:
#     n = int(input())
#     result = 0
#     if n == 0:
#         break
#     for num in range(n+1, 2*n+1):
#         count = 0
#         for j in range(2, num):
#             if num % j == 0:
#                 count+=1
#                 break
#         if count == 0:
#             result += 1
#     print(result)

#에라토스테네스의 체: https://leedakyeong.tistory.com/entry/python-소수-찾기-에라토스테네스의-체
import sys
import math
limit = 123456
eratos = [1] * (2 * limit + 1)
eratos[0] = 0
eratos[1] = 0

for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = 0
 
while 1:
    n = int(sys.stdin.readline())

    if n == 0:
      break
    else:
        print(sum(eratos[n+1:(2*n)+1]))