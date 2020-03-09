num1 = int(input())
num2 = int(input())
for n in map(int, list(str(num2)[::-1])):
    print(n * num1)
print(num1 * num2)

