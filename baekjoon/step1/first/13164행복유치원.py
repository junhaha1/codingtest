N, K = map(int, input().split())

childs = list(map(int, input().split()))

difs = []

for i in range(N - 1):
    difs.append(childs[i+1] - childs[i])

difs.sort()
result = sum(difs[:N-K])

print(result)