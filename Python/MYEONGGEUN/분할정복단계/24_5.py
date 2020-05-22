n,k=map(int,input().split())
d=1000000007
def c(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2>0:
        return c(a,b-1)*a
    else:
        x=c(a,b//2)
        x%=d
        return x**2%d
A=1
B=1
for i in range(1,n+1):
    A*=i
    A%=d
for i in range(1,k+1):
    B*=i
    B%=d
for i in range(1,n-k+1):
    B*=i
    B%=d
B=c(B,(d-2)%d)
print((A*B)%d)