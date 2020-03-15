def get_score(o):
    score = 0 
    for i in range(1, o.count('O') + 1):
        score += i
    return score


for _ in range(int(input())):
    ox = input()
    score = 0
    for o in ox.split('X'):
        score += get_score(o)
    print(score)