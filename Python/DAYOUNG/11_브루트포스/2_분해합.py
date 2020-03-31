N = int(input())

result = 0 
for i in range(N):
        num = list(map(int, str(i)))
        num_s = sum(num) + i
        if N == num_s:
            result = i
            break
if result == 0:
    print(0)
else:
    print(result)