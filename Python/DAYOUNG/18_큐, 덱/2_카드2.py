#시간초과
import sys

n = int(sys.stdin.readline())

queue = list(i for i in range(1, n+1))

while True:
    del queue[0]

    if len(queue) != 1:
        queue.append(queue[0])
        del queue[0]
    else:
        print(queue[0])
        break