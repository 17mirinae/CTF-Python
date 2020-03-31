N, M = map(int, input().split())
card = list(map(int, input().split()))

mx = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = card[i] + card[j] + card[k]
            if tmp <= M and tmp >= mx:
                mx = tmp

print(mx)
