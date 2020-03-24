import sys
cnt = int(input())
floor = []

for i in range(cnt):
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    H, W, N = map(int, sys.stdin.readline().split())
    # 나누어 떨어지는 경우 층수가 나오지 않음
    if N % H == 0:
        # 나누어 떨어지는 경우는 꼭대기 층이고, 몫이 방 번호가 됨
        tmp = H*100 + (N // H)
        floor.append(tmp)
    else:
        tmp = (N % H)*100 + (N // H) + 1
        floor.append(tmp)
        
for j in floor:
    print(j)
