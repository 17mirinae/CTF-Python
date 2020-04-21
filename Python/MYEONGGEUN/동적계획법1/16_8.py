n=int(input())
x=[n]
a=0
while True:
    if 1 in x:
        print(a)
        break
    calc=[]
    for i in x:
        if i%2==0:
            calc.append(i/2)
        if i%3==0:
            calc.append(i/3)
        calc.append(i-1)
    x=calc
    a+=1