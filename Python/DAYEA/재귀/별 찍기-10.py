def stars(n):    # 입력되는 배열의 인자는 3의 배수
    matrix = []
    for i in range(3 * len(n)):    # 3의 배수 만큼 실행
        if i//len(n) == 1:    # 
            matrix.append(n[i % len(n)] + " "*len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix

star = ["***", "* *", "***"]    # 기본 패턴
N = int(input())    # 3의 거듭 제곱
tmp = 0
while N != 3:    # 3인 경우 break (3인 경우는 이미 선언되어 있는 기본 패턴이므로)
    N = int(N/3)    # 3의 몇 제곱인지 파악하기 위해
    tmp += 1
    
for _ in range(tmp):
    star = stars(star)
for j in star:
    print(j)
