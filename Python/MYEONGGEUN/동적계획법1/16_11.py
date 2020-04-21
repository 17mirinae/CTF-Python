n=int(input())
a=list(map(int,input().split()))
x=[0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i]>a[j] and x[i]<x[j]:
            x[i]=x[j]
    x[i]+=1
print(max(x))