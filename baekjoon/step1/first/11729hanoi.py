n = int(input())

cnt = 0
result = []
def move(k, start, end):
  global cnt
  cnt += 1
  result.append((start, end))
def hanoi(k, start, end, sub):
  if k == 1:
    move(k, start, end)
    return 
  else:
    hanoi(k-1, start, sub, end)
    move(k, start, end)
    hanoi(k-1, sub, end, start)

    
hanoi(n, 1, 3, 2)  

print(cnt)
for r in result:
  print(*r, sep=" ")