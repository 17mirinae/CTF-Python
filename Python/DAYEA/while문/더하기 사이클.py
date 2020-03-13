N=int(input())
new=N
cycle=0
while True:
    cycle += 1
    temp = (new//10 + new%10) % 10
    new = (new%10)*10 + temp
    if N == new:
        break
print(cycle)
