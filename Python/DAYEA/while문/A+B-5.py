import sys
while True:
    A, B = map(int, sys.stdin.readline().split())
    # 파이썬의 if문에서 and와 or은 영어로 적는다.
    if A == 0 and B == 0:
        break
    print(A+B)
