N, M = map(int, input().split())
tree = list(map(int, input().split()))

mn, mx = 0, max(tree)
while mn <= mx:
    md = (mn + mx) // 2
    h = 0
    for i in tree:
        if i >= md:
            h += (i - md)
    if h >= M:
        result = md
        mn = md + 1
    else:
        mx = md - 1
        
print(result)
