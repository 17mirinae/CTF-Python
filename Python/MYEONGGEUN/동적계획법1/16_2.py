def fibonacci(n):
    l=len(zero)
    if l<=n:
        for i in range(l,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])
zero=[1,0]
one=[0,1]
a=int(input())
for i in range(a):
    n=int(input())
    fibonacci(n)