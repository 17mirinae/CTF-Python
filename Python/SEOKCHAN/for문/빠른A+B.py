import sys
input = lambda : sys.stdin.readline().strip()
for i in range(int(input())):
    print(sum(map(int, input().split())))
