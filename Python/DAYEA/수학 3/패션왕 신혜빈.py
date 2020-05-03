test = int(input())
for _ in range(test):
    dic = {}
    n = int(input())
    for __ in range(n):
        name, kind = input().split(' ')
        if not kind in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    sum = 1
    for i in dic.keys():
        sum *= (dic[i] + 1)
    print(sum - 1) # 혜빈이가 알몸이 아닌 상태이므로 하나를 뺀다.
