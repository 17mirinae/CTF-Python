n = int(input())

for i in range(n):
    num = input()
    score = 0
    plus = 0
    for j in range(len(num)):
        if num[j] == 'O':
            plus += 1
            score += plus
        else:
            plus = 0
    print(score)
            