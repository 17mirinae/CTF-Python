# Counter는 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체
from collections import Counter
S = input()
# 대소문자를 구분하지 않고, 대문자를 출력해야 하므로 문자열 전체를 대문자화
S = S.upper()
# most_common은 입력된 값의 요소들 중 빈도수가 높은 순으로 상위 n개를 리스트안의 투플 형태로 반환
result = Counter(S).most_common(2)
# 입력이 하나인 경우와 가장 많이 사용된 알파벳이 여러 개 존재하는 경우 예외 처리
if len(result) > 1 and result[0][1] == result[1][1]:
    print("?")
else:
    # 가장 빈도수가 높은 요소 출력
    print(result[0][0])
