from sys import stdin

input = stdin.readline

era = [False, False] + [True] * 999999

for i in range(2, 1000001):
  for j in range(2*i, 1000001, i):
    era[j] = False
    
while True:
  word = "Goldbach's conjecture is wrong."
  n = int(input().rstrip())
  if n == 0:
    break
  for i in range(3, n // 2 + 1):
    if era[i] == True and era[n-i] == True:
      word = str(n) + ' = ' + str(i) + ' + ' + str(n - i)
      break
  print(word)