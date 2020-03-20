def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x) 
    return int(n) + a
a= []
for i in range(1,10001):
    k = d(i)
    a.append(k)

for b in range(1, 10001):
    if b in a:
        pass
    else:
        print(b)

# https://claude-u.tistory.com/33
# 여집합