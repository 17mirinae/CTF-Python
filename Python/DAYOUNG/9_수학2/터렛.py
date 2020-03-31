import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    r_sum = r1 + r2

    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance > r_sum:
            print(0)
        elif distance == r_sum:
            print(1)
        elif distance < r_sum:
            if (distance+min(r1,r2)) == max(r1,r2):
                print(1)
                #한 원 안에서 접하는 경우
            elif (distance+min(r1,r2)) < max(r1,r2):
                print(0)
                #원 안에 들어가서 접점 없는 경우
            else:
                print(2)
                #이외에 두 점에서 만남
