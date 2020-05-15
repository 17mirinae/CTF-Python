for _ in range(int(input())):
    n,m=map(int,input().split())
    s=list(map(int,input().split()))
    q=[0 for _ in range(n)]
    q[m]=1
    cnt=0
    while True:
        if s[0]==max(s):
            cnt+=1
            if q[0]==1:
                print(cnt)
                break
            else:
                del s[0]
                del q[0]
        else:
            s.append(s[0])
            del s[0]
            q.append(q[0])
            del q[0]