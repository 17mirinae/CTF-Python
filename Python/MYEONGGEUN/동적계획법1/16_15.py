n=int(input())
a=list(map(int,input().split()))
x=[a[0]]
for i in range(len(a)-1):
    x.append(max(x[i]+a[i+1],a[i+1]))
print(max(x))