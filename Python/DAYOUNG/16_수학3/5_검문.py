#수의 개수
n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

#나눴을 때 똑같은 수인 M
#나머지가 같은 수의 집합체는 큰 수부터 정렬했을 때, 두 수의 차이가 일정하다는 뜻
#최대공약수 함수를 이용해 푸는 문제
#나머지가 같은 수를 구하고자 할 때, a, b, c, d(a>b>c>d)
#a-b, b-c, c-d 의 최대공약수를 구하고 해당 수의 약수를 출력해주면 된다.

num.sort(reverse= True)

#최대공약수를 빠르게 구해주는 유클리드 호제법
def gcd(x, y):
    mod = x % y
    while mod > 0 :
        x = y
        y = mod
        mod = x % y
    return y

#약수 리스트를 구해주는 함수
def div(x):
    div_list = [x]
    for i in range(2, int(x**(1/2)+1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i)
    div_list.sort()
    return div_list

#화물들의 차이 입력
diff = []
for i in range(len(num)-1):
    diff.append(num[i]-num[i+1])

#화물들의 차이를 최대공약수 함수를 이용해 구해주기
if len(diff) == 1:
    answer = diff[0]
elif len(diff) == 2:
    answer = gcd(diff[0], diff[1])
else:
    answer = diff[0]
    for i in range(1, len(diff)):
        answer = gcd(answer, diff[i])

#구한 최대공약수의 모든 약수 출력
for i in div(answer):
    print(i, end=' ')