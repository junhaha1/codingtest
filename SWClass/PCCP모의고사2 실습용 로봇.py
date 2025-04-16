def solution(Command):
  command = list(Command)
  answer = [0, 0]

  dis = [(0,1), (1, 0), (0, -1), (-1, 0)] # up, right, down, left
  
  i = 0
  for c in command:
    if c == 'G':
      answer[0] += dis[i][0]
      answer[1] += dis[i][1]
    if c == 'B':
      answer[0] -= dis[i][0]
      answer[1] -= dis[i][1]
    if c == 'R':
      i = (i + 1) % 4
    if c == 'L':
      i = (i - 1) % 4
  
  return answer

print(solution("GRGLGRG"))