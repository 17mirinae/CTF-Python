l = []
for i in range(10):
    a = int(input())
    if l.count(str(a%42)) < 1:
        l.append(str(a%42))
print(len(l))
