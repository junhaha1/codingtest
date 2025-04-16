from sys import stdin

input = stdin.readline

word = input().rstrip()

def check():
  l = 0
  r = len(word) - 1
  while l < r:
    if word[l] != word[r]:
      return 0
    l += 1
    r -= 1
  return 1

print(check())
    