# 주어진 크로아티아 알파벳을 리스트화
L = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
for word in L:
    if word in S:
        # 크로아티아 알파벳이 S문자열 안에 있다면, a로 변경
        S = S.replace(word, "a")
# a로 변경했으므로, 하나의 문자로 볼 수 있어 문자열의 길이로 알파벳의 개수를 구할 수 있음
print(len(S))

그룹 단어 체커.py
N = int(input())
S = []
for i in range(N):
    S.append(input())
for j in S:
	tmp = [j[0]]
	for k in range(1, len(j)):
		# 연속되지 않지만, 이전에 사용된 알파벳이라면 그룹 단어가 아니므로 break
		if j[k-1] != j[k] and j[k] in tmp:
			N -= 1
			break
		else:
			tmp.append(j[k])
			continue
print(N)
