from collections import deque
N, M = map(int, input().split())
L = deque(range(1, N+1))
A = list(map(int, input().split()))

total = 0
for a in A:
    i = 0
    while a != L[i]:
        i += 1
    if i < len(L)-i:
        i = -i
    else:
        i = len(L)-i
    L.rotate(i)
    total += abs(i)
    L.popleft()
    
print(total)
