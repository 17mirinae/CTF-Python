def f(n,m,k):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            if(visited[i] == 0):
                visited[i] = 1
                res[n] = arr[i]
                print(res)
                f(n+1,m,k)
                visited[i] = 0

n, m = map(int, input().split())

arr = range(1,n+1)
res = [0] * m
visited = [0 for i in range(n)]
f(0,n,m)
