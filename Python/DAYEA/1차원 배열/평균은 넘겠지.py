import sys
N=int(input())
per=[]
for i in range(N):
    cnt = 0
    L = list(map(int, sys.stdin.readline().split()))
    # 배열의 첫번째 원소는 학생 수
    avg = sum(L[1:])/L[0]
    for j in L[1:]:
        if j > avg:
            cnt += 1
    # 평균 이상의 비율 구하기
    tmp = (cnt/L[0]) * 100
    # round함수를 통해 소수3번째 자리까지 반올림
    per.append(round(tmp, 3))
for x in per:
    # %를 출력하기 위해서는 %%
    print("%.3f%%" %x)
