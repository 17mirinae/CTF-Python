start = input()
start = '0' * (2 - len(start)) + start


def calc(arg):
    (a, b) = map(int, list(arg))
    result = a + b
    return str(b) + str(result % 10)


tmp = start
i = 1
while True:
    tmp = calc(tmp)
    if tmp == start:
        break
    i += 1

print(i)