#시간초과
import sys

statements = sys.stdin.read().splitlines()
statements = statements[1:]

def size(queue):
    print(len(queue))

def empty(queue):
    if queue:
        print("-1")
    else:
        print("0")

def front(queue):
    if queue:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if queue:
        print(queue[-1])
    else:
        print(-1)

queue = []
for string in statements:
    string = sys.stdin.readline()
    if string.find('push') != -1:
        queue.append(int(string[4:]))
    elif string == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print("-1")
    else:
        eval(string + "(queue)")