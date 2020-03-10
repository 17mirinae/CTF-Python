a = int(input())
b = int(input())

r1 = a*(b%10)
r2 = a*((b%100)//10)
r3 = a*(b//100)

r = a*b
print(r1, r2, r3, r, sep="\n")