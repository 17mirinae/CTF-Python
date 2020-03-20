for _ in range(int(input())):
    r, text = input().split()
    tmp = ''.join([t * int(r) for t in text])
    print(tmp)
