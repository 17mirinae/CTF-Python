# https://chancoding.tistory.com/33
n = int(input())

goal = []
number = []
for i in range(n):
    goal.append(int(input()))
    number.append(i+1)

stack = []
result = []
out = True
for i in goal:
    while True:
        if stack and stack[-1] > i:
            out = False
        if not stack or stack[-1] != i:
            stack.append(number.pop(0))
            result.append('+')
        if stack and stack[-1] == i:
            stack.pop()
            result.append('-')
            break
if out != False:
    print('\n'.join(result))
else:
    print("NO")