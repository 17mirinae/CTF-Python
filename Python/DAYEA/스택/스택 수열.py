n = int(input())
stack = []
L = []
i = 1
 
while(n > 0):
    n -= 1
    sequence = int(input())
    #스택이 비어있다면 하나 채워준다
    if len(stack)==0:
        stack.append(i)
        L.append("+")
        i += 1
 
    while(stack[-1] < sequence):#스택의 탑보다 sequence가 크면
        stack.append(i)
        L.append("+")
        i += 1
    if stack[-1] == sequence: #같다면 pop
        stack.pop()
        L.append("-")
    elif stack[-1] > sequence: #스택의 탑보다 sequence가 작다면 불가능
        L = []
        L.append("NO")
        break
        
for l in L:
    print(l)
