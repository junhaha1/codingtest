N, L = map(int, input().split())
holes = list(map(int, input().split()))

holes.sort()

distance = holes[0] + L - 0.5
count = 1

for i in range(1, N):
    if distance >= holes[i] + 0.5:
        continue
    elif distance < holes[i] + 0.5:
        distance = holes[i] + L - 0.5
        count += 1

print(count)