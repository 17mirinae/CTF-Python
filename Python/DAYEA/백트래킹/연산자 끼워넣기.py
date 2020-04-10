import sys
import itertools
 
def setOperator(N, add, sub, mul, div):
    operator = [] 
    for i in range(N-1):
        if add > 0:
            operator.append("+")
            add -= 1
        elif sub > 0:
            operator.append("-")
            sub -= 1
        elif mul > 0:
            operator.append("*")
            mul -= 1
        elif div > 0:
            operator.append("/")
            div -= 1
    return operator
 
def solve(N, A, operator):
    result = A[0]
    # 연산자를 위한 인덱스이므로 N보다 하나작은 범위를 가진다.
    for i in range(N-1):
        if operator[i] == "+":
            result += A[i+1]
        elif operator[i] == "-":
            result -= A[i+1]
        elif operator[i] == "*":
            result *= A[i+1]
        elif operator[i] == "/":
            # 나눈 값의 int로 형변환을 하여 소숫점 아래 자릿수를 버림
            result = int(result / A[i+1])
    return result

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

L = setOperator(N, add, sub, mul, div)
operators = list(itertools.permutations(L))

maxVal = -sys.maxsize
minVal = sys.maxsize
 
for operator in operators:
    result = solve(N, A, operator)  # 연산자의 순열을 구함
 
    if result < minVal:
        minVal = result
       
    if result > maxVal:
        maxVal = result

print(maxVal)
print(minVal)
