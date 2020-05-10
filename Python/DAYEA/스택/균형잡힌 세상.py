import sys
input = sys.stdin.readline

while True:
    cmd = input().rstrip()
    stack = []
    flag = True
    for i in cmd:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
    if cmd == '.':
        break
    print("yes" if flag and not(stack) else "no")
