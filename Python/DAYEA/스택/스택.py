import sys
input = sys.stdin.readline
N = int(input())
<<<<<<< HEAD
stack = list()
for i in range(N):
    cmd = input()
    print(cmd)
    if cmd.split()[0] == 'push':
        stack.append(cmd.split()[1])
    elif cmd == 'pop':
=======
stack = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
>>>>>>> 49fcd13757e07acaf1f5c7a2530780e47f0baa60
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if not stack:
            print(1)
        else :
            print(0)
    elif cmd[0] == "top":
        if not stack:
            print(-1)
        else :
            print(stack[-1])

