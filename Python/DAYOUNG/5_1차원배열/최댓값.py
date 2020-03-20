numbers = []
m = 0
for i in range(9):
    numbers.append(int(input()))
    if numbers[i] >m:
        m = numbers[i]
        n = i
print(m)
print(n+1)