#시간초과
# n = int(input())
# stack = []
# for i in range(n):
#     string = input()
#     if string == 'push':
#         stack.append(int(input()))
#     elif string == 'pop':
#         if not stack:
#             print(-1)  
#         else:
#             print(stack[-1])
#             stack.pop(-1)
#     elif string == 'size':
#         print(len(stack))
#     elif string == 'empty':
#         if not stack:
#             print(1)
#         else:
#             print(0)
#     elif string == 'top':
#         if not stack:
#             print(-1)
#         else:
#             print(stack[-1])

import sys

statements = sys.stdin.read().splitlines()
statements = statements[1:]

stack = []

def size(stack):
    print(len(stack))

def empty(stack):
    r = 0 if stack else 1
    print(r)

def top(stack):
    r = stack[-1] if stack else -1
    print(r)

for s in statements:
    if s.find('push') != -1:
        stack.append(int(s[4:]))
    elif s == 'pop':
        r = stack.pop() if stack else -1
        print(r)
    else:
        eval(s + "(stack)")