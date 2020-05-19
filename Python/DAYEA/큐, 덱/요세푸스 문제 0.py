N, K = map(int, input().split())
L = list(range(1, N+1))
result = []
k = K-1

while True:
    result. append(L.pop(k))
    if not L:
        break
    k = (k+K-1) % len(L)
    
print('<'+', '.join(map(str, result))+'>')
