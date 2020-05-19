from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
que = deque()

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.popleft()
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif cmd[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
