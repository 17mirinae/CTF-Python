a=int(input())
x=[0 for _ in range(a+1)]
x[1]=1
for i in range(2,a+1):
    x[i]=x[i-1]+x[i-2]
print(x[-1])
