(_, standard) = map(int, input().split())
for i in [x for x in map(int, input().split()) if x < standard]:
    print(i, end=" ")