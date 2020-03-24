for _ in range(int(input())):
    x, y = map(int, input().split())
    X = int((y-x-1)**0.5)
    print(2*X+1 if y-x > X**2+X else 2*X)