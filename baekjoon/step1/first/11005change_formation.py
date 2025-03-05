from sys import stdin

input = stdin.readline

n, b = map(int, input().split())
result = ''

while n != 0:
    if n % b > 9:
        result = chr(55 + n % b) + result
    else:
        result = str(n % b) + result
    n //= b

print(result)