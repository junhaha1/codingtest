N = int(input())
seq = list(map(int, input().split()))

left = 0
right = N - 1

zero = abs(seq[left] + seq[right])
result = [seq[left], seq[right]]

while left != right:
  temp = seq[left] + seq[right]

  if abs(temp) < zero:
    zero = abs(temp)
    result[0] = seq[left]
    result[1] = seq[right]
    
  if temp >= 0:
    right -= 1

  if temp < 0:
    left += 1
    
print(*result)