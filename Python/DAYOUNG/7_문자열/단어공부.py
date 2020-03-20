string = input().upper()
p = [0 for _ in range(26)]

#ASCII A: 65 ~ Z: 90
for i in range(len(string)):
    m = int(ord(string[i])) - 65
    p[m] += 1

r = [i for i, x in enumerate(p) if x == max(p)]

if int(len(r))>1:
    print("?")
else:
    print(chr(p.index(max(p))+65))