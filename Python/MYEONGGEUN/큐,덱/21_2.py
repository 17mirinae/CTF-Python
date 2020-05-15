import sys
from collections import deque
q=deque()
for i in range(int(input())):
    q.append(i+1)
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(q[0])