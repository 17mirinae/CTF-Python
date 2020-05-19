# https://upcount.tistory.com/5

x = int(input())
mat = [input() for _ in range(x)]

def quad(x1, y1, n):
    if n == 1:
        return mat[y1][x1]
    a = n //2
    
    r1 = quad(x1, y1,  a)
    r2 = quad(x1+a, y1, a)
    r3 = quad(x1, y1+a, a)
    r4 = quad(x1+a, y1+a, a)

    if r1 == r2 == r3 == r4 and len(r1) == 1:
        return r1
    return "(" + r1 + r2 + r3 + r4 + ")"

print(quad(0,0,x))

# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011