N = int(input())
L = list(map(int, input().split()))
# max(L)을 for문 안에서 사용하면 에러가 발생하므로 변수로 
mx = max(L)
total = 0
for i in range(N):
    total += (L[i]/mx)*100
print(total/N)
