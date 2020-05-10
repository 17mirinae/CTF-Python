#틀렸음 : 에제2 
# t = int(input())
# for _ in range(t):
#     stack = []
#     vps = list(input())
#     for s in vps:
#         if s == "(":
#             stack.append(1)
#         elif s == ")":
#             stack.append(-1)
#     if sum(stack) == 0:
#         print("YES")
#     else:
#         print("NO")

#pop으로 해야함

t = int(input())
for _ in range(t):
    stack = []
    vps = list(input())
    for s in vps:
        if s == "(":
            stack.append(0)
        elif s == ")":
            if stack:
                del stack[-1]
            else:
                stack.append(-1)
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
