num =[int(input()) for i in range(3)]
number = num[0] * num[1] * num[2]
tmp = list(str(number))
N = list(map(int, tmp))
for i in range(10):
    print(N.count(i))
