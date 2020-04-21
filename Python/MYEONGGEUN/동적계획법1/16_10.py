n=int(input())
w=[0]
for i in range(n):
    w.append(int(input()))
x=[0]
x.append(w[1])
if n>1:
    x.append(w[1]+w[2])
for i in range(3,n+1):
    x.append(max(x[i-1],x[i-3]+w[i-1]+w[i],x[i-2]+w[i]))
print(x[n])