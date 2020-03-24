# 높이: V 미터, 낮: +A 미터, 밤: -B 미터
# 정상까지 얼마나 걸리는 지 출력

A, B, V = map(int, input().split())

#day*A - (day-1)*B >= V
#day >= (V-B)/(A-B)

day = (V-B)/(A-B)
print(int(day) if day == int(day) else int(day)+1) #day = 4.3일 경우, int(day) = 5