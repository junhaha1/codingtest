N = int(input())
weight = list(map(int, input().split()))
weight.sort()

target = 1
for w in weight:
    if w > target:
        break
    target += w

print(target)