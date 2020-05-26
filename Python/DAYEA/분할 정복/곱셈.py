A, B, C = map(int, input().split())
# a=nc+r이라고 생각햇을때
# a^2=(nc)^2+2(nc)r+r^2
# a^2를 c로 나눈것의 나머지는 r^2%c
def square(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 1:
        return square(a, b-1) * a
    else:
        d = square(a, b//2)
        d %= C
        return (d**2) % C

print(square(A, B) % C)
