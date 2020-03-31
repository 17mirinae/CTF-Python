def hanoi(n, start, mid, end):
    if n == 1:
        move.append([start,end])
    else:
        hanoi(n-1,start,end,mid)
        move.append([start,end])
        hanoi(n-1,mid,start,end)

#N-1 원판을 중간에 모두 놓고 제일 큰 원판을 3으로 옮김 - n-1원판을 2에서 3으로,,,

N = int(input())
move = []
hanoi(N, 1,2,3)
print(len(move))
for i in move:
    print(move[i][0], move[i][1])

#https://leedakyeong.tistory.com/entry/백준-python-11729번-하노이-탑-이동-순서hanoi-top-in-python