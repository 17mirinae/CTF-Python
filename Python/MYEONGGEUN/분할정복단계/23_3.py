n=int(input())
p=[list(map(int,input().split()))for _ in range(n)]
a=0
b=0
c=0
def f(x,y,n):
    global a,b,c
    check=p[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if p[i][j]!=check:
                for k in range(3):
                    for l in range(3):
                        f(x+k*n//3,y+l*n//3,n//3)
                return
    if check==-1:
        a+=1
    elif check==0:
        b+=1
    else:
        c+=1
f(0,0,n)
print(a)
print(b)
print(c)
