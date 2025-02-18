n, s, r = map(int, input().split())

ds = list(map(int, input().split()))

ar = list(map(int, input().split()))

teams = [1 for _ in range(n)]

for i in ds:
    teams[i-1] -= 1

for i in ar:
    teams[i-1] += 1

for i in range(n):
    if teams[i] == 2 and 0 <= i - 1 and teams[i-1] == 0:
        teams[i-1] += 1
        teams[i] -= 1
    if teams[i] == 2 and i + 1 < n and teams[i + 1] == 0:
        teams[i+1] += 1
        teams[i] -= 1

print(teams.count(0))

