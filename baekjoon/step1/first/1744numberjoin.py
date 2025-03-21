from sys import stdin

input = stdin.readline
n = int(input())

num1 = [] #양수
zero = 1 #0의 갯수
num2 = [] #음수

for _ in range(n):
  temp = int(input())
  if temp == 0:
    zero = 0
  elif temp > 0 :
    num1.append(temp)
  elif temp < 0:
    num2.append(temp)
    
num1.sort(reverse=True)
num2.sort()

def calc1(num):
  temp = 0
  if len(num) % 2 != 0:
    temp += num[-1]
    num = num [:-1]
    
  for i in range(1, len(num), 2):
    temp += max(num[i-1] * num[i], num[i-1] + num[i])
  return temp

def calc2(num, zero):
  temp = 0
  if len(num) % 2 != 0:
    temp += zero * num[-1]
    num = num[:-1]
    
  for i in range(1, len(num), 2):
    temp += num[i-1] * num[i]
  return temp

n1, n2 = calc1(num1), calc2(num2, zero)


print(n1 + n2)
      
      
    
  