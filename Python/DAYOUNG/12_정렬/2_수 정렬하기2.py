import sys
l = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
#sys.stdout.write("\n".join(map(str, sorted(l))))