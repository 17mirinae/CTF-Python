N = int(input())
dungchi = []

for _ in range(N):
    w, h = map(int, input().split())
    dungchi.append((w,h))

for i in dungchi:
    result = 1
    for k in dungchi:
        if i[0] < k[0] and i[1] < k[1]:
            result += 1
    print(result, end=" ")
