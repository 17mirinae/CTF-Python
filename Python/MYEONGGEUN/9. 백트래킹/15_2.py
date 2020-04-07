from itertools import combinations
a,b=map(int,input().split())
C=combinations(range(1,a+1),b)
for i in C:
    print(' '.join(map(str,i)))