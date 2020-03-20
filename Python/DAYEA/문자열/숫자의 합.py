N = int(input())
# 문자열로 받아서 리스트 취급이 가능하도록
A = input()
B = 0
for i in range(N):
    B += int(A[i])
print(B)
