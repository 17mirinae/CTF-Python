#5543

min_h = 2000
min_d = 2000

for i in range(3):
    h = int(input())
    min_h = min(min_h, h)

for i in range(2):
    d = int(input())
    min_d = min(min_d, d)

print(min_d+min_h-50)