n = int(input())

people = list(map(int, input().split()))

if n == 1:
    print(people[0])
else:
    #정렬 -> 누적되는 시간이 줄어든다.
    people.sort()

    i_sum = 0
    min_sum = 0

    for i in range(n):
        #i_sum에는 이전 사람들이 돈을 인출하는데 걸렸던 시간을 포함 + people[i]는 현재 사람이 돈을 인출하는데 걸리는 시간
        # = 한 사람이 돈을 인출하는데 걸리는 전체 시간
        min_sum += (i_sum + people[i])

        #i_sum에 현재 사람이 인출하는 데 걸리는 시간을 더하여 다음 사람 순서의 min_sum 계산에 반영할 수 있도록 한다.
        i_sum += people[i]
    
    print(min_sum)