import sys

t = int(sys.stdin.readline())
def p(n):
    answer = 0
    p_list = [0, 1, 1, 1, 2, 2]

    if n <= 5:
        print(p_list[n])
    else:
        for i in range(6, n+1):
            answer = p_list[i-5] + p_list[i-1]
            p_list.append(answer)
        print(answer)

for _ in range(t):
    p(int(sys.stdin.readline()))