n=int(input())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
w=0
b=0
def h(x,y,n):
    global w,b
    c=m[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if c!=m[i][j]:
                h(x,y,n//2)
                h(x,y+n//2,n//2)
                h(x+n//2,y,n//2)
                h(x+n//2,y+n//2,n//2)
                return
    if c==0:
        w+=1
    else:
        b+=1
h(0,0,n)
print(w)
print(b)