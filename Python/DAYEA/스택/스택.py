import sys
input = sys.stdin.readline
N = int(input())
stack = list()
for i in range(N):
    cmd = input()
    print(cmd)
    if cmd.split()[0] == 'push':
        stack.append(cmd.split()[1])
    elif cmd == 'pop':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if not stack:
            print('1')
        else:
            print('0')
    elif cmd == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])

