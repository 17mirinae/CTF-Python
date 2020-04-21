a=list(str(input()))
b=list(str(input()))
x=[[0 for _ in range(len(a)+1)]for _ in range(len(b)+1)]
y=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            x[j+1][i+1]=x[j][i]+1
            y=max(y,x[j+1][i+1])
        else:
            x[j+1][i+1]=max(x[j][i+1],x[j+1][i])
print(y)