# 알파벳을 미리 선언
A = "abcdefghijklmnopqrstuvwxyz"
S = input()
for i in A:
    # find()함수를 통해 알파벳 중에 S에 존재하는 것이 없으면 -1, 있으면 S의 몇번째 자리에 있는지를 출력
    print(S.find(i), end=" ")
