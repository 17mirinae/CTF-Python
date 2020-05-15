import queue

#데이터 추가 put()
#첫번째 원소 제거 q.get() - 제거할때 원소를 반환

# 1 2 3 4 5 6 7 - 3
# 4 5 6 7 1 2 - 3 6 
# 7 1 2 4 5 - 3 6 2 
# 4 5 7 1 - 3 6 2 7
# ....

n, k = map(int, input().split())

q = queue.Queue()

number = list(i for i in range(n))

while len(number) > 0:
    if k < len(number):    
        q.get(number[k])
        del number[k]
        k += 2
    else:
        k -= len(number)
        q.get(number[k])
        del number[k]

print(q)
