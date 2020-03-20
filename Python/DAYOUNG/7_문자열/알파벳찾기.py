s = input() #소문자 <= 100
p = [-1 for _ in range(26)]
#ASCII a: 97 ~ z: 122
for j in range(len(s)):
    m = int(ord(s[j])) - 97
    if p[m] == -1:
        p[m] = j
for i in range(26):
	print(p[i], end=' ')