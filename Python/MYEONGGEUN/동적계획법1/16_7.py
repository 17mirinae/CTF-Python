n=int(input())
a=[0 for i in range(301)]
x=[0 for i in range(301)]
for i in range(n):
    a[i]=int(input())
x[0]=a[0]
x[1]=a[0]+a[1]
x[2]=max(a[1]+a[2],a[0]+a[2])
for i in range(3,n):
    x[i]=max(x[i-3]+a[i-1]+a[i],x[i-2]+a[i])
print(x[n-1])