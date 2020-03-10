# //은 몫을 구하는 연산자
a=int(input())
b=int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)
