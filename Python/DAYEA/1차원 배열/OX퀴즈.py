import sys
N=int(input())
score=[]
for i in range(N):
    # 매 반복시 사용되므로 for문의 시작에서 초기화
    # 점수 계산을 위한 변수
    tmp = 0
    # 맞을 경우를 위한 
    con = 1
    ox = sys.stdin.readline()
    for j in range(len(ox)):
        if ox[j] == 'O':
            tmp += con
            con += 1
        else:
            con = 1
    score.append(tmp)
for x in score:
    print(x)
