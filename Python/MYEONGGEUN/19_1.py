while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    if b%a==0:
        print('fartor')
    elif a%b==0:
        print('multiple')
    else:
        print('neither')