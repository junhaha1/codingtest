from sys import stdin

input = stdin.readline
n = int(input())

chains = list(map(int, input().split()))
chains.sort()

tc = 1

for chain in chains:
    if tc + chain >= n:
        break
    else:
        tc += chain
        n -= 1
        
        
print(n - 1)