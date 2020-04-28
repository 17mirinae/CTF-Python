import sys

#진짜 약수의 개수
num = int(sys.stdin.readline())

#n의 진짜 약수
number = list(map(int, sys.stdin.readline().split()))

#조건: N은 a의 배수 and A는 1과 N이 아님 -> 약수의 최대값 * 최소값
number.sort()
print(number[0] * number[-1])
