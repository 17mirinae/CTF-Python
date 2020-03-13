t = int(input())

ab = [input() for x in range(t)]

for x in range(t):
    print("Case #%d: %s + %s = %d" %(x+1, ab[x][0], ab[x][2], int(ab[x][0])+int(ab[x][2])))