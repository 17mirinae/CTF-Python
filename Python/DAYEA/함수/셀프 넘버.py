def d(n):
    ret = n
    for i in str(n):
        ret += int(i)
    return ret
    
# set은 집합 자료형
A = set(range(1, 10001))
B = set()

# 1~10001의 숫자를 d함수를 적용하여 B집합에 넣어줌
for i in range(1,10001):
    B.add(d(i))
# 여집합을 통해 A와 B가 가진 동일한 원소들을 삭제
A = A - B
# 집합을 배열로 변환
C = list(A)
# 오름차순으로 
C.sort()
for j in C:
    print(j)
