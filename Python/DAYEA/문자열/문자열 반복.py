import sys
N = int(input())
for i in range(N):
    R, S = sys.stdin.readline().split()
    R = int(R)
    # 문자열을 리스트처럼 취급
    for i in S:
        # 문자*정수를 출력하면 문자가 해당 정수의 크기만큼 반복해서 출력됨
        print(i*R, end="")
    print("")
