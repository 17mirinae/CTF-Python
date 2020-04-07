from itertools import combinations
a=int(input())
x=[]
for _ in range(a):
    x.append(list(map(int,input().split())))
n=[i for i in range(a)]
res=float('inf')
def A():
    global res
    for i in combinations(n,a//2):
        member_a=list(i)
        member_b=list(set(n)-set(i))
        comb_a=list(combinations(member_a,2))
        comb_b=list(combinations(member_b,2))
        sum_a=0
        for j,k in comb_a:
            sum_a+=(x[j][k]+x[k][j])
        sum_b=0
        for j,k in comb_b:
            sum_b+=(x[j][k]+x[k][j])
        if res>abs(sum_a-sum_b):
            res=abs(sum_a-sum_b)
A()
print(res)