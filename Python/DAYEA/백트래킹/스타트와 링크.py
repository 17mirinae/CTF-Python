import sys
from itertools import combinations

def DFS(n, s):   
    L = [_ for _ in range(n)]
    result = 100
    
    # 팀이 될 수 있는 모든 조합(set)의 배열
    for i in combinations(L, n // 2):
        
        # 선택된 후보(start)와 나머지(link)
        start = list(i)
        link = list(set(L) - set(i))
        
        # 점수 비교는 2명씩 이루어진다.
        start_comb = list(combinations(start, 2))
        print(start_comb)
        link_comb = list(combinations(link, 2))
        print(link_comb)

        # 점수 구하기
        start_sum = 0
        for x, y in start_comb:
            start_sum += (s[x][y] + s[y][x])
            
        link_sum = 0
        for x, y in link_comb:
            link_sum += (s[x][y] + s[y][x])
        
        # 차이를 구하는 것이므로 절댓값 사용
        if result > abs(start_sum - link_sum):
            result = abs(start_sum - link_sum)

    return result

N = int(input())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(S)

print(DFS(N, S))
