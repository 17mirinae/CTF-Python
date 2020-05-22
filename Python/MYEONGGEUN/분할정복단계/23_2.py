n=int(input())
m=[input()for _ in range(n)]
def h(x,y,n):
    if n==1:
        return m[y][x]
    q1=h(x,y,n//2)
    q2=h(x,y+n//2,n//2)
    q3=h(x+n//2,y,n//2)
    q4=h(x+n//2,y+n//2,n//2)
    if q1==q2==q3==q4 and len(q1)==1:
        return q1
    return "("+q1+q2+q3+q4+")"
print(h(0,0,n))