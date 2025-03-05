from sys import stdin
from math import ceil

input = stdin.readline

num = int(input().rstrip())

result = ''

while num != 0 and num != 1:
    result = str(abs(num % -2)) + result
    num = ceil(num / -2)

result = str(num) + result

print(result)
