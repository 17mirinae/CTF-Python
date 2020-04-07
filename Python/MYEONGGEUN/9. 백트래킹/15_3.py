a,b=map(int,input().split())
x=[]
def A(c,a,b):
    if c==b:
        print(' '.join(map(str,x)))
        return
    for i in range(a):
        x.append(i+1)
        A(c+1,a,b)
        x.pop()
A(0,a,b)