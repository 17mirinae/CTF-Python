import sys

# 에라토스테네스의 체 이용
L = [1] * (123456*2+1)
L[0] = 0
L[1] = 0
end = (123456*2) ** 0.5 + 1
for i in range(2, int(end)):
    if L[i] == 1:
        for j in range(i+i, 123456*2+1, i):
            L[j] = 0
 
while True:
    n=int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(sum(L[n+1:(2*n)+1]))
