class stack:
    def __init__(self):
        self.len=0
        self.list=[]
    def push(self,x):
        self.list.append(x)
        self.len+=1
    def pop(self):
        if self.size()==0:
            return -1
        self.len-=1
        return self.list.pop()
    def size(self):
        return self.len
    def top(self):
        return self.list[-1] if self.size() else -1
    def empty(self):
        return 1 if len (self.list)==0 else 0
n=int(input())
in_list=[int(input())for _ in range(n)]
out_list=[]
p=0
stack=stack()
for i in range(n):
    stack.push(i+1)
    out_list.append('+')
    while p<n and stack.top()==in_list[p]:
        stack.pop()
        out_list.append('-')
        p+=1
if not stack.empty():
    print('NO')
else:
    for i in out_list:
        print(i)