import math
A, B, V = map(int, input().split())

# V에서 A를 뺐으므로 하루를 더하고, 하루가 지나고 이동한 값으로 나눈 값을 올림
# 나눈 값이 소수점이라고 해도, 그 값은 이동한 것이므로 올림을 하여야 함
print(math.ceil((V-A)/(A-B))+1)
