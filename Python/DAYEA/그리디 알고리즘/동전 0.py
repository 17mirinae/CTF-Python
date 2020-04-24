N, K = map(int, input().split())
L = [int(input()) for _ in range(N)]

num = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if L[i] > K:
        continue    # 아래의 코드를 실행하지 않고 다음 i로 넘김
    num += K // L[i]
    K %= L[i]

print(num)
