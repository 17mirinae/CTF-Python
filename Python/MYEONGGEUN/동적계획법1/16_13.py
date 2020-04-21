n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
a=sorted(a,key=lambda x:x[0])
x=[0 for _ in range(n)]
x[0]=1
for i in range(1,n):
    min_x=0
    for j in range(i):
        if a[i][1]>a[j][1]:
            min_x=max(x[j],min_x)
    x[i]=min_x+1
print(n-max(x))