#숏코드
# string = [sum([int(plus) for plus in minus.split('+')]) for minus in input().split('-')]
# print(string[0]-sum(string[1:]))
#처음 입력을 받을 때부터 +와 -으로 split하고, int로 숫자를 받음으로써 문제 해결
#https://claude-u.tistory.com/210


#입력 : 55-50+40
string = []
for m in input().split('-'):
    # m = 55, 50+40
    #'-'를 기준으로 문자열을 나눈다.
    num = 0
    for p in m.split('+'):
        num += int(p)
        #string 배열에 p의 합들을 넣어 줌
        #string: 55, 90
        # string = [sum(int(p))] -> 오류: TypeError: 'int' object is not iterable
    string.append(num)

print(string[0]-sum(string[1:]))

#예제가 55-50+40-30+20 인 경우 출력이 옳게 되는가? => -85 옳게 되는 듯ㄴ