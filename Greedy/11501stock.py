from sys import stdin

input = stdin.readline
t = int(input())

result = []
for i in range(t):
    total = 0
    day = int(input())
    prices = list(map(int, input().split()))

    #prices.reverse()로 해도 가능
    m = 0
    for j in prices[::-1]:
        if j >= m:
            m = j
        elif j < m:
            total += m - j
    result.append(total)
for t in result:
    print(t)