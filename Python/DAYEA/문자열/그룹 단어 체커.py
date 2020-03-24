N = int(input())
S = []
for i in range(N):
    S.append(input())
for j in S:
	tmp = [j[0]]
	for k in range(1, len(j)):
		if j[k-1] != j[k] and j[k] in tmp:
			N -= 1
			break
		else:
			tmp.append(j[k])
			continue
print(N)
