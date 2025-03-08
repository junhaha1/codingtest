from sys import stdin

dp = [[0, 0], [0, 1]]


for i in range(2, int(input()) + 1):
    dp.append([dp[-1][0] + dp[-1][1], dp[-1][0]])

print(sum(dp[-1]))