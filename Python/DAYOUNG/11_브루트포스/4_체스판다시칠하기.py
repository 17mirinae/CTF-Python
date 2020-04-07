#https://leedakyeong.tistory.com/entry/백준-1018번-체스판-다시-칠하기-in-python-파이썬

# N, M = map(int, input().split(' '))
# matrix = []
# paint = 0
# start_x_index = 0
# start_B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
# start_W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

# for _ in range(N) :
#     matrix.append(list(input()))

# if matrix[0][0] == 'W' :
#     for x in range(N) :
#         if x%2 == 0 and matrix[x] != start_W :
#             for y in range(M) :
#                 if matrix[x][y] != start_W[y] :
#                     paint += 1
#         elif x%2 == 1 and matrix[x] != start_B
# else : # 시작이 'B'라면
#     for x in range(N) :
#         if matrix[x] != start_B :
#             for y in range(M) :
#                 if matrix[x][y] != start_B[W] :
#                     paint += 1

# print(paint)
# [출처] 백준_1018_체스판 다시 칠하기_파이썬_브루트포스(완전탐색)|작성자 가나다라아차