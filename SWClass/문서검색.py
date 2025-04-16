from sys import stdin

input = stdin.readline

word = input().rstrip()

s2= input().rstrip()

n = len(word)
m = len(s2)

cnt = 0
i = 0

while i < (n - m + 1):
  if word[i:i+m] == s2:
    cnt += 1
    i += m
  else:
    i += 1

print(cnt)