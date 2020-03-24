A, B, C = map(int, input().split())

# 노트북 가격이 가변 비용보다 작은 경우는 절대 손익분기점을 넘길 수 없기 때문
if C > B :
    # 노트북 가격과 가변 비용의 차액이 고정 비용을 넘는 순간이 손익분기점이 됨
    N = (A//(C-B))+1
    print(N)
else:
    print(-1)
