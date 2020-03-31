def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        # 가장 큰 원반(n)을 end로 옮기기 위해 n-1개의 원반을 mid로 이동
        hanoi(n - 1, start, end, mid)
        print(start, end)
        # mid에 있는 n-1개의 원반을 end로 이동
        hanoi(n - 1, mid, start, end)

N = int(input())
cnt = 0

for _ in range(N):
    cnt *= 2    # 1이상의 경우 hanoi 함수를 두번씩 실행하므로
    cnt += 1

print(cnt)
hanoi(N, 1, 2, 3)
