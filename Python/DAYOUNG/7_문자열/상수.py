A, B = input().split()
a = int("".join(map(str, list(reversed(A)))))
b = int("".join(map(str, list(reversed(B)))))
print(a) if a>b else print(b)

#join: 리스트를 문자열로, ""는 리스트 값 사이에 들어갈 문자열