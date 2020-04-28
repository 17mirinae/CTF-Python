A, B = map(int, input().split())

def GCD(x,y):    # 유클리드 호제법
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y    
    
def LCM(x, y):
    return x * y // GCD(x,y)

print(GCD(A, B))
print(LCM(A, B))
