N, X = map(int, input().split())
# map형식으로 나누어진 것을 list로 형변환하여 for문이 편해지도록 함
L = list(map(int, input().split()))
for i in range(N):
    if X > L[i]:
        print(L[i], end=" ")
