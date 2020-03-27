while 1:
        line = []
        a, b, c = map(int, input().split())
        if a == 0:
            break
        line.append(a)
        line.append(b)
        line.append(c)
        line.sort()
        if line[0]*line[0] + line[1]*line[1] == line[2]*line[2]:
            print("right")
        else:
            print("wrong")