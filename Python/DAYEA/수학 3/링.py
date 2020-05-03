from fractions import Fraction 
N = int(input())
L = list(map(int, input().split()))

for i in range(1, N):
    answer = Fraction(L[0],1)/Fraction(L[i],1)
    print("%d/%d" % (answer.numerator, answer.denominator))
