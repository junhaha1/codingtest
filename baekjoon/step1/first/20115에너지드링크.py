N = int(input())

drinks = list(map(int, input().split()))

drinks.sort(reverse=True)

result = drinks[0]

for i in range(1, N):
    result += drinks[i] / 2

print(result)