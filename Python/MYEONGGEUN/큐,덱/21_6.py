n,m=map(int,input().split())
s=list(map(int,input().split()))
q=[i+1 for i in range(n)]
cnt=0
for i in range(m):
    qlen=len(q)
    qindex=q.index(s[i])
    if qindex<qlen-qindex:
        while True:
            if q[0]==s[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt+=1
    else:
        while True:
            if q[0]==s[i]:
                del q[0]
                break
            else:
                q.insert(0,q[-1])
                del q[-1]
                cnt+=1
print(cnt)