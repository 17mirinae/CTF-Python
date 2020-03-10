#큰 경우에는 '>', 작은 경우에는 '<', 같은 경우에는 '=='를 출력
a,b=map(int, input().split())
if(a>b):
    print(">")
elif(a<b):
    print("<")
elif(a==b):
    print("==")
