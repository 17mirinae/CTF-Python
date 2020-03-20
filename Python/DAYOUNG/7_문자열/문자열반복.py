import sys
test = int(input())
for j in range(test):
    r, s = input().split()
    
    for i in range(len(s)):
        print(s[i]*int(r), end='')
    print("")

    