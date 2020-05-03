import math
n=int(input())
m=[]
k=[]
gcd=0
for i in range(n):
    m.append(int(input())
    if i==1:
        gcd=abs(m[1]-m[0])
    gcd=math.gcd(abs(m[i]-m[i-1]),gcd)
gcdk=int(gcd**0.5)
for i in range(2,gcdk+1):
    if gcd%i==0:
        k.append(i)
        k.append(gcd//i)
k.append(gcd)
k=list(set(k))
k.sort()
for i in k:
    print(i,end='')