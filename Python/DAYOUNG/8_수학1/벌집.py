N = int(input())

compare = 1
plus = 6
room = 1
if N == 1:
    print(1)
else:
    while 1:
        compare += plus
        room += 1
        if N <= compare:
            print(room)
            break
        plus += 6

# 1, 7, 19, 37, 61 ...
#  +6, +12, +18, +24
#    +6   +6   +6
# N < 7 -> 2개