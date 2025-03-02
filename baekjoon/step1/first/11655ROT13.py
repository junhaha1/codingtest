from sys import stdin

string = input()
result = ''

for s in string:
  if 'a' <= s <= 'z':
    num = ord(s) + 13
    if num > ord('z'):
      result += chr(ord('a') + (num-123))
    else:
      result+= chr(num)
  elif 'A' <= s <= 'Z':
    num = ord(s) + 13
    if num > ord('Z'):
      result += chr(ord('A') + (num-91))
    else:
      result+= chr(num)
  else:
    result += s
print(result)