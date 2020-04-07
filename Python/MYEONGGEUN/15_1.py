from itertools import permutations
a,b=map(int,input().split())
P=permutations(range(1,a+1),b)
for i in P:
    print(' '.join(map(str,i)))