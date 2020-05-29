
# 메모리 초과
# n = int(input())
# k = int(input())

# B = []
# for i in range(1, n+1):
#     for j in range(1, n+1):

#         B.append(i*j)

# B.sort()
# print(B[k])

# https://claude-u.tistory.com/449

n, k = int(input()), int(input*())
start, end = 1, k

while start <= end:
    mid = (start + end) //2

    temp = 0
    for i in range(1, n+1):
        # mid 이하의 i의 배수 or 최대 n
        temp += min(mid//i, n)

    #이분탐색 실행
    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)