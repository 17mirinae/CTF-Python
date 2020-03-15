t = int(input())
scores = list(map(int, input().split()))
m = max(scores)
print(sum([(s/m) * 100 for s in scores])/t)
