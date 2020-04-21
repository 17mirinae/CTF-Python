n = int(input()) #전깃줄 개수

line = []

for _ in range(n):
    a, b = map(int, input().split())
    line.append([a, b])

#A 오름차순 정렬
line = sorted(line, key= lambda x : x[0])

#왜 b의 가장 긴 증가 수열을 구하는 거지...? 
# => 교차하지 않을려면 B가 작은 것부터 수열을 이뤄야함
# ex) 큰 수가 작은 수 보다 앞부분에 위치하면 교차하게 된다. 1-5, 3-3 -> 교차

result = [ [] for _ in range(n)] #2차원 배열 만들기
for i in range(n):
    if i == 0:
        result[i].append(line[i][1]) #시작값
    else:
        for j in range(0, i):
            if result[j][-1] < line[i][1]:

                #왜 이걸 하는지 모르겠음/없으면 틀림
                #i가 j보다 길면, b(전깃줄)값을 넣을 필요가 없기 때문이다.
                if len(result[i]) - 1 < len(result[j]):
                    result[i] = result[j] + [line[i][1]]
        if not result[i]:
            result[i].append(line[i][1])
    print("result[",i ,"]", result[i])


#가장 긴 수열
maximum = 0
for i in range(n):
    maximum = max(maximum, len(result[i]))
print(n - maximum)