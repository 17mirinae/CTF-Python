t = int(input())

a_b = [input() for i in range(t)]

for i in range(t):
    print("Case #%d: %d" %(i+1, int(a_b[i][0])+int(a_b[i][2])))