n=int(input())
x=[]
for i in range(n):
    x.append(list(map(int,input().split())))
a=2
for i in range(1,n):
    for j in range(a):
        if j==0:
            x[i][j]=x[i][j]+x[i-1][j]
        elif i==j:
            x[i][j]=x[i][j]+x[i-1][j-1]
        else:
            x[i][j]=max(x[i-1][j-1],x[i-1][j])+x[i][j]
    a+=1
print(max(x[n-1])) 