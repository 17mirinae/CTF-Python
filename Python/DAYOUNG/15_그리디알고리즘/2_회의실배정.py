n = int(input()) #회의의 수

times = []
for _ in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

#끝나는 시간 기준 오름차순 정렬
times = sorted(times, key= lambda x : [x[1], x[0]])

start = answer = 0
for m in times:
    print(m)
    if start <= m[0]:
        start = m[1]
        answer += 1
print(answer)
