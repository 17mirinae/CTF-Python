Test = int(input())
for i in range(Test):
    floor, rooms, guest = map(int, input().split()) #층의 개수, 층 당 방의 개수, 몇 번째 손님인지
    n = guest%floor #층수
    m =  guest//floor + 1 #호수
    if n == 0:
        m -= 1
        n = floor
    print(n*100+m)
