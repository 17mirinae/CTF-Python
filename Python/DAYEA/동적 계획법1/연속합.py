N = int(input())
A = list(map(int, input().split()))
summ = [A[0]]
for i in range(N - 1):
    # 연속된 수를 더한 값과 새로운 값을 비교하여,
    # 새로운값이 더크다면 새로운 값을 선택하여 다시 연속된 수의 합을 시작
    summ.append(max(summ[i] + A[i + 1], A[i + 1]))
print(max(summ))
