n, x = map(int, input().split())
number = list(map(int, input().split()))

for i in range(n):
    if number[i] < x :
        print(number[i], end=' ')