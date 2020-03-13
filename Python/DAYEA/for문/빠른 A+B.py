# sys.stdin.readline()를 사용하기위해 import
import sys
N= int(input())
for i in range(N):
    # 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다.
    # 따라서, input()대신 sys.stdin.readline()을 사용한다.
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
