N = int(input())

if N % 5 == 0: # 5로 나누어 떨어지면 전부 5로
    ans = N // 5
elif N % 5 == 1: # 6이 남는 꼴
	ans = (N // 5) + 1    # 3*2 = 5*1 + 1
elif N >= 12 and N % 5 == 2: # 12가 남는 꼴
	ans = (N // 5) + 2    # 3*4 = 5*2 + 2
elif N % 5 == 3: # 3이 남는 꼴
	ans = (N // 5) + 1
elif N >= 9 and N % 5 == 4: # 9가 남는 꼴
	ans = (N // 5) + 2    # 3*3 = 5*1 + 4
else:
	ans = -1

print(ans)
