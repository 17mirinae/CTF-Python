cnt_0 = [1, 0]
cnt_1 = [0, 1]
for i in range(2,41):
    cnt_0.append(cnt_0[i-1]+cnt_0[i-2])
    cnt_1.append(cnt_1[i-1]+cnt_1[i-2])
    
T = int(input())
N = [int(input()) for _ in range(T)]
for n in N:
    print(cnt_0[n], cnt_1[n])
