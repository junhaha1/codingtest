from sys import stdin
input = stdin.readline


n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

x = []
for i in range(n - 1):
    x.append(sensors[i + 1] - sensors[i])
x.sort()

print(sum(x[:n-k]))

