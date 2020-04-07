a=int(input())
n=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
y,x=1e9,-1e9
def A(i,res,add,sub,mul,div):
    global x,y
    if i==a:
        x=max(res,x)
        y=min(res,y)
    else:
        if add:
            A(i+1,res+n[i],add-1,sub,mul,div)
        if sub:
            A(i+1,res-n[i],add,sub-1,mul,div)
        if mul:
            A(i+1,res*n[i],add,sub,mul-1,div)
        if div:
            A(i+1,int(res/n[i]),add,sub,mul,div-1)
A(1,n[0],add,sub,mul,div)
print(x)
print(y)