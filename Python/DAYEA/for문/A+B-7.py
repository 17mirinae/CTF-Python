import sys
N= int(input())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    # C와 유사하게 문자열안에 변수에 맞춰서 넣고, %(,,)안에 해당하는 변수명을 순서대로 넣어준다.
    print("Case #%d: %d" % (i+1, A+B))
