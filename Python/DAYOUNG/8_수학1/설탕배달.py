#설탕 봉지 3kg or 5kg
#최대한 적은 개수 봉지 들고 가기 - 출력

# N = int(input())

# if N//5 == 0:
#     print(-1)
# elif N%5 == 0:
#     print(N//5)
# elif N%5 > 5:
#     m = N//5
#     N = N - (N//5)*5
#     if N%3 == 0:
#         print(m + N//3)
#     else:
#         print(-1)
# else:
#     if N%3 == 0:
#         print(N//3)
#     else:
#         print(-1)
###### 예제 입출력 5가 적용이 안됨 ######

N = int(input())
B = 0 #봉지 개수
while 1:
    if N%5 == 0: #5kg 봉지에 빠짐없이 담을 수 있다면
        print(B+N//5)
        break
    else: #5kg 봉지에 빠짐없이 담을 수 없다면
        N = N-3 #3kg 봉지에 한 번 담기
        B += 1
        if N < 0:
            print(-1)
            break
