import sys
input = sys.stdin.readline

def AC(P, L):
    rev = True
    if len(L) < P.count('D'):
        return 'error'
    for i in P:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            idx = 0 if rev else -1
            if L:
                L.pop(idx)
            else:
                return 'error'
    if L:
        if rev:
            return '[' + ','.join(L) + ']'
        else:
            return '[' + ','.join(reversed(L)) + ']'
    else:
        return '[]'

T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    l = input()
    l = list(''.join(l[1:-2]).split(","))
    if n == 0: l = []
    print(AC(p, l))
