def div(a,b):
    c=0
    while a!=0:
        a=a//b
        c+=a
    return c
n,m=list(map(int,input().split()))
f=div(n,5)-div(m,5)-div(n-m,5)
t=div(n,2)-div(m,2)-div(n-m,2)
print(min(f,t))