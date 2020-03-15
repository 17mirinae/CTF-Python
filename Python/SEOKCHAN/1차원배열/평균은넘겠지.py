def parse(line):
    n = int(line.split(' ')[0])
    scores = list(map(int, line.split(' ')[1:]))
    return (n, scores)

for _ in range(int(input())):
    (n, scores) = parse(input())
    average = sum(scores) / n
    over_average = len([s for s in scores if s > average])
    print("{:.3%}".format(over_average / n))