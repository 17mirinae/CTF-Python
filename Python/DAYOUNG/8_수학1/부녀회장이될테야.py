Test = int(input())
for i in range(Test):
    k = int(input()) #층
    n = int(input()) #호
    rooms = [i for i in range(1, n+1)] #1층의 1호~n호
    for _ in range(k):
        for j in range(1, n):
            rooms[j] += rooms[j-1]
    print(rooms[n-1])


