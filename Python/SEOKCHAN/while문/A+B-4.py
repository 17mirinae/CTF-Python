import sys
for t in [x.strip() for x in sys.stdin.readlines()]:
    print(sum(map(int, t.split())))