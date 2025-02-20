from sys import stdin

input = stdin.readline
t = int(input())

for i in range(t):
    total = 0
    stock = []
    day = int(input())
    prices = list(map(int, input().split()))
    for j in range(len(prices)):
        if prices[j] == min(prices[j:len(prices)]) or prices[j] < max(prices[j:len(prices)]):
            stock.append(prices[j])
        elif prices[j] == max(prices[j:len(prices)]):
            total += (prices[j] * len(stock)) - sum(stock)
            stock.clear()
    print(total)
            
