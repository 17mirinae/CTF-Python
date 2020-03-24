N = int(input())
    
for i in range(N):
    k = int(input())
    n = int(input())
    # 1~n까지의 수가 들어있는 배열
    base=[j for j in range(1,n+1)]
    for _ in range(k):
        for m in range(1,n):
            # room[k-1, n] + room[k, n-1]
            base[m]+=base[m-1]
    # 배열의 시작이 0부터 이므로 n-1번째를 출력해준다.
    print(base[n-1])
