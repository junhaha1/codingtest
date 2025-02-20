from sys import stdin
input = stdin.readline

n = int(input())
rank = []
for _ in range(n):
    rank.append(int(input()))
    
rank.sort()
result = 0
for i in range(n):
    if rank[i] != i + 1:
        result += abs(rank[i] - (i+1))
print(result)
        