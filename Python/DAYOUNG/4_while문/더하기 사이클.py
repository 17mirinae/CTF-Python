# 0<= n <= 99

m = n = int(input())

num = 1
while 1:
    ten = int(m)//10
    one = int(m)%10
    new = ten+one
    m = str(one) + str(new%10)

    if(n == int(m)):
        break
    else:
        num += 1
print(num)