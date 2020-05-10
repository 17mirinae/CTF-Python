n, m = map(int, input().split())

# 최대공약수, 최소공배수 출력

#유클리드 호제법
def gcd(x,y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

def lcm(x,y):
    return x * y // gcd(x,y)

print(gcd(n,m))
print(lcm(n,m))