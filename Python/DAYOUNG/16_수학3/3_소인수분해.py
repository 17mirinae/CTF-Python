n = int(input())

i = 2
while 1:
    if n % i == 0:
        n = n // i
        print(i)
    else:
        i += 1
    
    if n == 1:
        break

