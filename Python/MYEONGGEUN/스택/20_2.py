k=int(input())
z=[]
for _ in range(k):
    n=int(input())
    if n==0:
        z.pop()
    else:
        z.append(n)
print(sum(z))