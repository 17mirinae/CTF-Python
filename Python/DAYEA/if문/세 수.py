#두 번째로 큰 정수를 출력하는 프로그램
num=list(map(int, input().split()))
num.sort()  # 입력이 4개 이상일 결우에는 reverse=True를 sort함수안에 입력
print(num[1])
