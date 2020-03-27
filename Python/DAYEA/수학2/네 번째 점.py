x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

ans = [x[0], y[0]]
if x[1] == x[2]: pass
elif x[0] == x[1]: ans[0] = x[2]
else: ans[0] = x[1]

if y[1] == y[2]: pass
elif y[0] == y[1]: ans[1] = y[2]
else: ans[1] = y[1]

print(ans[0], ans[1])
