n=int(input())
for i in range(n):
    for j in range(i+1):
        # 파이썬의 print문은 줄바꿈을 포함하고 있으므로, end=""를 통해 한줄에 출력될 수 있도록 함
        print("*", end="")
    # 줄바꿈을 해줌
    print("")
