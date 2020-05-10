#틀렸음: ([)] 을 고려하지 못함
# import sys

# string = list(sys.stdin.readline())
# while string != ".":
#     small = []
#     big = []
#     for s in string:
#         if s == "(":
#             small.append(1)
#         elif s == ")":
#             if len(small) == 0:
#                 small.append(-1)
#                 break
#             else:
#                 del small[-1]
#         elif s == "[":
#             big.append(1)
#         elif s == "]":
#             if len(big) == 0:
#                 big.append(-1)
#                 break
#             else:
#                 del big[-1]
#     if len(small) == 0 and len(big) == 0:
#         print("yes")
#     else:
#         print("no")

#     string = list(sys.stdin.readline())

while True:
    string = input()
    if string == ".":
        break
    stack = []
    answer = True

    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                answer = False
                break
        elif s == "]":
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                answer = False
                break
    if answer and not stack:
        print("yes")
    else:
        print("no")