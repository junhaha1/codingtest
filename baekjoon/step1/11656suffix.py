from sys import stdin

input = stdin.readline
words = input().rstrip()
result = []

for i in range(len(words)):
  result.append(words[i::])
  
result.sort()

for r in result:
  print(r)