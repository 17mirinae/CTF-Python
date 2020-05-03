a,b=map(int,input().split())
def ggcf(a,b):
    x=a if a>=b else b
    y=b if x==a else a
    if x%y==0:
        return y
    else:
        while x%y:
            gcf=x%y
            x=y
            y=gcf
        return gcf
gcf=ggcf(a,b)
lcm=(a*b)//gcf
print(f'{gcf}\n{lcm}')