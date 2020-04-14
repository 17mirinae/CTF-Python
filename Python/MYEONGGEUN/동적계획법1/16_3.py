a=int(input())
x=[0]*1000001
x[1],x[2]=1,2
def tile(n):
    for i in range(3,n+1):
        x[i]=(x[i-2]+x[i-1])%15476
tile(a)
print(x[a])