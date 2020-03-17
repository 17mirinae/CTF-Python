a = int(input())
b = int(input())
c = int(input())
abc = list(str(a*b*c))

for i in range(10):
    print(abc.count(str(i)))
# count() : 리스트에 해당 문자가 몇 개씩 있는지 출력