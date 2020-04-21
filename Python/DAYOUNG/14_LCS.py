#https://suri78.tistory.com/11
import sys

s1 = sys.stdin.readline().strip().upper()
s2 = sys.stdin.readline().strip().upper()

len1 = len(s1)
len2 = len(s2)

#2차원 배열 
matrix = [ [0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1+1):
    for j in range(1, len2 + 1):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else: #기존에 주어진 문자열로 만들 주 있는 최대 길이
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])