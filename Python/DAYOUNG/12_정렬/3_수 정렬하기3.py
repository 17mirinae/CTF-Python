# import sys
# l = [int(input()) for _ in range(int(sys.stdin.readline()))]
# sys.stdout.write("\n".join(map(str, sorted(l))))
# #메모리초과

# #미리 정의된 리스트 사용
# import sys
# N = int(input())
# series = [0] * 10001

# for i in range(N):
#     a = int(sys.stdin.readline())
#     series[a] = series[a] + 1
#     #series 배열의 a(입력값)번째에 값이 있음( +1 )을 나타냄
#     #동일한 입력값이 여러 개 일 때, series[a]의 값은 1보다 큼

# for k in range(len(series)):
#     if series[k] != 0:
#         for j in range(series[k]):
#             print(k)

#딕셔너리 사용
import sys
N = int(input())
dic = {}
for i in range(N):
    a = int(sys.stdin.readline())
    if a in dic:
        dic[a] = dic[a] + 1
    else:
        dic[a] = 1
for s in sorted(dic.items()):
    for i in range(s[1]):
        print(s[0])