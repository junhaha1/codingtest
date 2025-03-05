n = int(input())

result = 1
for i in range(1, n + 1):
    result *= i

cnt = 0
while True:
  if result % 10 != 0:
    break
  result //= 10
  cnt += 1
  
print(cnt)
# cnt = 0
# for r in str(result)[::-1]:
#    if r != '0':
#      break
#    cnt += 1
   
# print(cnt)