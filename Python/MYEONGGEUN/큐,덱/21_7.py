for _ in range(int(input())):
    p=input()
    aclen=int(input())
    if aclen==0:
        ac=input()
        ac=[]
    else:
        ac=list(map(int,input()[1:-1].split(',')))
    rev=False
    check=True
    front=0
    back=0
    for j in p:
        try:
            if j=='R':
                rev=not rev
            elif j=='D' and not rev:
                front+=1
            elif j=='D' and rev:
                back+=1
        except:
            check=False
            print('error')
            break
    if check:
        if front+back<=aclen:
            if not rev:
                ac=ac[front:aclen-back]
                print(str(ac).replace(' ',''))
            else:
                ac=ac[::-1][back:aclen-front]
                print(str(ac).replace(' ',''))
        else:
            print('error')