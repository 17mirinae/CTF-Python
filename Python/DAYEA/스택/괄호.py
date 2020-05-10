N = int(input())
for _ in range(N):
    VPS = list(input())
    cnt = 0
    for i in VPS:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')
