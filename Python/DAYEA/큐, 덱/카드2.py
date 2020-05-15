from collections import deque
N = int(input())
L = deque([_ for _ in range(1, N+1)])
while len(L) > 1:
    L.popleft()
    tmp = L[0]
    L.popleft()
    L.append(tmp)
print(*L)
