N = int(input())
numbers = list(map(int, input().split()))
num = 0 #소수 개수
for i in numbers:
    if i > 1:
        n = 0
        for j in range(2, i): #소수는 2 ~ i-1까지의 수로는 나눠져선 안됨
            if i % j == 0: 
                n += 1
        if n == 0:
            num += 1
            
print(num)