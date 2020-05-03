#분수함수인 fractions모듈의 Fraction을 이용하여 최대공약수를 빠르게 계산
from fractions import Fraction
n=int(input())
count=list(map(int,input().split()))
for i in range(1,n):
    x=Fraction(count[0],count[i])
    print(x.numerator,'/',x.denominator,sep='')
'''
numerator 분자를 가져옴
denominator 분모를 가져옴
sep='' 출력간 띄어쓰기를 공백으로 바꿔줌
'''