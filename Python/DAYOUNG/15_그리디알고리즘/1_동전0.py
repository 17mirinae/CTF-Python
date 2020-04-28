n , k = map(int, input().split())

a = [ int(input()) for _ in range(n)]

count = 0

for i in range(1, n+1):
    #인덱스 끝부터 순회 : 마이너스 인덱스
    #큰 값부터 갯수를 세는 것이 동전 개수의 최솟값을 계산하는데 효율적
    coin = a[-i] 
    
    if k >= coin:
        num = k // coin # num은 coin(동전)의 개수
        k -= coin * num # coin(동전)의 개수만큼 k에서 빼줌 -> 나머지 값
        count += num

print(count)