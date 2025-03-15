from sys import stdin, maxsize
from itertools import product

input = stdin.readline

ch = int(input())

if int(input()) > 0:
  nb = list(map(int, input().rstrip().split()))
else:
  nb = []
  
min_mov = abs(100 - ch)
  
for nums in range(1000001):
  nums = str(nums)
  for j in range(len(nums)):
    if int(nums[j]) in nb:
      break
    elif j == len(nums) - 1:
      min_mov = min(abs(int(nums) - ch) + len(nums), min_mov) 
      
print(min_mov)
    

