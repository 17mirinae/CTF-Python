a,b=map(int,input().split())
x=[]
def A(c,d,a,b):
    if c==b:
        print(' '.join(map(str,x)))
        return
    for i in range(d,a):
        x.append(i+1)
        A(c+1,i,a,b)
        x.pop()
A(0,0,a,b)