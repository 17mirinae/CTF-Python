# 문자열로 이루어진 리스트로 받음
L = input().split()
for i in range(len(L)):
    # 문자열을 리스트화 하여 역순으로 정렬
    tmp = list(L[i])
    tmp.reverse()
    # '(연결 문자)'.join()함수를 이용하여 리스트를 문자열로 변환
    tmp = ''.join(tmp)
    # 해당 문자열을 다시 정수로 변환
    L[i] = int(tmp)
# 두 수의 크기 비교
if L[0] >= L[1]:
    print(L[0])
else:
    print(L[1])
