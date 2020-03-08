a = input()
b = input()

def func(num):
    sum = 0
    for i in range(0, 3):
        sum += int(a[i]) * int('1'+'0'*i) * num
    return sum

print(func(int(b[0])))
print(func(int(b[1]) * 10))
print(func(int(b[2]) * 100)))

