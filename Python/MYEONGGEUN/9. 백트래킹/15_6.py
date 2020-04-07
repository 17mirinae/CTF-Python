import sys
s=[list(map(int,input().split()))for _ in range(9)]
zero=[(i,j)for i in range(9)for j in range(9)if s[i][j]==0]
def sdk(d):
    if d==len(zero):
        for i in s:
            print(*i)
        sys.exit(0)
    else:
        x=zero[d][0]
        y=zero[d][1]
        dx=(x//3)*3
        dy=(y//3)*3
        n=[False]+[True for _ in range(9)]
        for j in range(9):
            if s[x][j]:
                n[s[x][j]]=False
            if s[j][y]:
                n[s[j][y]]=False
        for i in range(dx,dx+3):
            for j in range(dy,dy+3):
                check=s[i][j]
                if check:
                    n[check]=False
        c=[i for i,k in enumerate(n)if k]
        for i in c:
            s[x][y]=i
            sdk(d+1)
            s[x][y]=0
sdk(0)