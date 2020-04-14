l=[0,1,1,1]
def P(n):
    if len(l)<=n:
        for i in range(len(l),n+1):
            l.append(l[i-2]+l[i-3])
    print(l[n])
a=int(input())
for _ in range(a):
    n=int(input())
    P(n)