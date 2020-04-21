n=int(input())
a=list(map(int,input().split()))
x=[0 for i in range(n)]
y=[0 for i in range(n)]
z=[0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i]>a[j] and x[i]<x[j]:
            x[i]=x[j]
    x[i]+=1
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[i]>a[j] and y[i]<y[j]:
            y[i]=y[j]
    y[i]+=1
for i in range(n):
    z[i]=x[i]+y[i]-1
print(max(z))