N = int(input())
seq = list(map(int, input().split()))

left = 0
right = N - 1

zero = int(1e9)
left_result = 0
right_result = 0

while left != right:
  temp = seq[left] + seq[right]
  if abs(temp) < zero:
    left_result = left
    right_result = right
    zero = abs(temp)
  if temp >= 0:
    right -= 1
  else:
    left += 1
    
print(seq[left_result], seq[right_result])