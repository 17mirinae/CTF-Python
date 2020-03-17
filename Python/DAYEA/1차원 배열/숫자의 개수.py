num =[int(input()) for i in range(3)]
# 곱한 값을 구함
number = num[0] * num[1] * num[2]
# 구한 값을 문자열로 바꾼 후 리스트로 바꾸어줌
tmp = list(str(number))
# 해당 리스트의 요소를 숫자로 변환
N = list(map(int, tmp))
for i in range(10):
    # count함수를 사용하여 0~9까지의 숫자가 각각 몇가 있는 지 출력
    print(N.count(i))
