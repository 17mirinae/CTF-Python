N = int(input())
dp = [N]
cnt = 0

while True:
    if 1 in dp:
        print(cnt)
        break
    calc = []
    # 순서를 알 수 없으므로 모든 수에 적용한다는 생각으로 진행
    for i in dp:
        if i % 2 == 0:
            calc.append(i / 2)
        if i % 3 == 0:
            calc.append(i / 3)
        calc.append(i - 1)
    dp = calc
    cnt += 1
