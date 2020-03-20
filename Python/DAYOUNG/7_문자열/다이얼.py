dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)
#https://j-remind.tistory.com/76

#숏코딩
# print(sum(min(ord(c)-64,25)*28//89+3for c in input()))
# https://sssunho.tistory.com/50

