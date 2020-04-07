N = int(input())

l = [int(input()) for _ in range(N)]
l.sort()
for i in range(N):
    print(l[i])