import sys
a,b=int(sys.stdin.readline()),0
x,y,z=[False]*a,[False]*(2*a-1),[False]*(2*a-1)
def A(i):
    global b
    if i==a:
        b+=1
        return
    for j in range(a):
        if not x[j] and not y[i+j] and not z[i-j+a-1]:
            x[j]=y[i+j]=z[i-j+a-1]=True
            A(i+1)
            x[j]=y[i+j]=z[i-j+a-1]=False
A(0)
print(b)