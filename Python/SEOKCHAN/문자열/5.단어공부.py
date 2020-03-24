text = input().lower()
alphabets = list(set(text))
status = {}
for a in alphabets:
    status[a] = text.count(a)

if list(status.values()).count(max(status.values())) != 1:
    print("?")
else:
    print(max(status, key=status.get).upper())
