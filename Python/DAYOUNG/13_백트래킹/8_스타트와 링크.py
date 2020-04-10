#뭔소리야,,,
#https://m.post.naver.com/viewer/postView.nhn?volumeNo=26831431&memberNo=33264526

import sys
import math
from itertools import combinations

#4<=n<=20, n은 짝수
n = int(sys.stdin.readline())
maps = [] #2차원배열
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

#두 개의 그룹으로 나눌 사람의 리스트
people = list(range(n))

#두 개의 그룹으로 나누기. n명 중 n//2명을 선택하는 경우의 수
candidate = list(combinations(people, n//2))

answer = math.inf

for group in candidate:
    #해당 그룹에 속하지 않은 나머지 사람들의 리스트
    rest = list(set(people)-set(group))
    
    group_sum, rest_sum = 0, 0

    #두 명씩 짝지어 시너지를 확인해야 하므로, 다시 두 명씩 짝지어준다
    group_combination = list(combinations(list(group),2))
    rest_combination = list(combinations(rest, 2))

    for y, x in group_combination:
        group_sum += (maps[y][x] + maps[x][y])
    
    for y, x in rest_combination:
        rest_sum += (maps[y][x] + maps[x][y])
    
    #두 그룹의 합계 차이가 최소가 되도록 구한다.
    if answer > abs(group_sum - rest_sum):
        answer = abs(group_sum - rest_sum)

print(answer)