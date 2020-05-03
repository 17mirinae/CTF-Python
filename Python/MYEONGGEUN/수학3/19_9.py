for i in range(int(input())):
    x={}
    s=1
    for j in range(int(input())):
        a,b=input().split()
        if not b in x:
            x[b]=1
        else:
            x[b]+=1
    for k in x.keys():
        s=s*(x[k]+1)
    print(s-1)