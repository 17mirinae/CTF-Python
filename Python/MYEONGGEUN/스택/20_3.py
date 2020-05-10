t=int(input())
for i in range(t):
    vps=list(input())
    n=0
    while len(vps)!=0:
        if n<0:
            break
        x=vps.pop()
        if x=='(':
            n-=1
        elif x==')':
            n+=1
    if n==0:
        print('YES')
    else:
        print('NO')