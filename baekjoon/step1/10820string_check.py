from sys import stdin

while True:
  try:
    string = list(input())
    result = [0, 0, 0, 0]
    for s in string:
      if 'a' <= s <= 'z':
        result[0] += 1
      elif 'A' <= s <= 'Z':
        result[1] += 1
      elif '0' <= s <= '9':
        result[2] += 1
      elif s == ' ':
        result[3] += 1
    print(*result)
  except EOFError:
    break


while True:
  string = stdin.readline().rstrip('\n')
  
  if not string: #종료하기
    break
  
  result = [0, 0, 0, 0]
  for s in string:
    if s.islower(): result[0] += 1
    elif s.isupper(): result[1] +=1
    elif s.isdigit(): result[2] += 1
    elif s.isspace(): result[3] += 1
  print(*result)