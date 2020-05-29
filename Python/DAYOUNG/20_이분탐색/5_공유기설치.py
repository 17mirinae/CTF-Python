import sys

n, c = map(int, input().split())

house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

# https://claude-u.tistory.com/448

# 첫 집을 start, 첫 집과 끝 집의 차이를 end
start, end = 1, house[-1] - house[0]

#해당 거리를 유지하며 공유기가 몇 개 설치 될 수 있는지
def router_counter(distance):
    count = 1
    cur_house = house[0] #시작점
    for i in range(1, n):
        # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
        if cur_house + distance <= house[i]:
            count += 1
            cur_house = house[i] #공유기 설치된 집 갱신
    return count

while start <= end:
    mid = (start + end) //2
    if router_counter(mid) >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid -1

print(answer)