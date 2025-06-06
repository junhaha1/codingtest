from sys import stdin

input = stdin.readline

K = int(input())
rope = []

for _ in range(K):
    rope.append(int(input()))

rope.sort(reverse=True)
result = 0
for _ in range(K):
    result = max(result, len(rope) * rope.pop())

print(result)