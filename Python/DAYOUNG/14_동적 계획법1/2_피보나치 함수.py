a = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]

def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(zero[i-1]+zero[i-2])
    print(zero[num], one[num])

for i in range(a):
    k = int(input())
    cal(k)

#정답, 리스트를 만들고 시작하는게 맘에 안듦
# def fibonacci(n):
#     zero_count = [1, 0]
#     one_count = [0, 1]
#     if n <= 1:
#         return
#     for i in range(2, n+1):
#         zero_count.append(zero_count[i-1]+zero_count[i-2])
#         one_count.append(one_count[i-1]+one_count[i-2])
#     return zero_count, one_count

# n = int(input())
# zero, one = fibonacci(40)

# for _ in range(n):
#     m = int(input())
#     print(zero[m], one[m])

#시간초과
# import sys
# zero = 0
# one = 0
# def fibo(n):
#     global zero, one
#     if n == 0 :
#         zero += 1
#         return 0
#     elif n == 1 :
#         one += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# for _ in range(int(sys.stdin.readline())):
#     zero = 0
#     one = 0
#     N = int(sys.stdin.readline())
#     fibo(N)
#     print(zero, one)

###############################################

#시간초과
# import sys
# T = int(sys.stdin.readline())
# fibo = [(1,0), (0,1)]

# def fibonacci(n, index):
#     global fibo
#     if n < 2:
#         return fibo[n][index]
#     else:
#         return fibonacci(n-1, index) + fibonacci(n-2, index)

# for _ in range(T):
#     n = int(sys.stdin.readline())
#     print(fibonacci(n, 0), fibonacci(n, 1))