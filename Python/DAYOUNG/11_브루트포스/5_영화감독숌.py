N = int(input())
six = 666
cnt = 0
while 1:
    if '666' in str(six):
        cnt += 1
    if cnt == N:
        break
    six = six + 1
print(six)