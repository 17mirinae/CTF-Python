# 파일의 끝(EOF)을 올바르게 판단하는 법을 연습
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# sys모듈을 사용한 경우
import sys
 
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)
