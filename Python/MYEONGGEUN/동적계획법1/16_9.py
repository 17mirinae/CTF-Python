n=int(input())
x=[[0 for i in range(10)]for j in range(101)]
for i in range(1,10):
    x[1][i]=1
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            x[i][j]=x[i-1][1]
        elif j==9:
            x[i][j]=x[i-1][8]
        else:
            x[i][j]=x[i-1][j-1]+x[i-1][j+1]
print(sum(x[n])%1000000000)