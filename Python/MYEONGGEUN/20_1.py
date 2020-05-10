import sys
def push(n):
    s.append(n)
def pop():
    try:
        print(s.pop())
    except:
        print(-1)
def size():
    return len(s)
def empty():
    print(1) if size()==0 else print(0)
def top():
    try:
        print(s[-1])
    except:
        print(-1)
n=int(sys.stdin.readline().rstrip())
s=[]
for _ in range(n):
    c=sys.stdin.readline().rstrip().split()
    if c[0]=='push':
        push(c[1])
    elif c[0]=='pop':
        pop()
    elif c[0]=='size':
        print(size())
    elif c[0]=='empty':
        empty()
    elif c[0]=='top':
        top()