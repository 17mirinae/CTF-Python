import string
text = input()
for c in string.ascii_lowercase:
    print(text.find(c), end=" ")
