moneys = [500, 100, 50, 10, 5, 1]

m = int(input())
total = 1000 - m

result = 0

for money in moneys:
    result += total // money
    total %= money
print(result)