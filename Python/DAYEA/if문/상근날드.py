A=int(input())
B=int(input())
C=int(input())
a=int(input())
b=int(input())
if( A <= B ): burger=A
else: burger=B
if( burger <= C ): burger=burger
else: burger=C
if( a <= b ): drink=a
else: drink=b
print(burger+drink-50)

# 더 간단하게
burger =[int(input()) for i in range(3)]
drink =[int(input()) for i in range(2)]
print(min(burger) + min(drink) - 50)
