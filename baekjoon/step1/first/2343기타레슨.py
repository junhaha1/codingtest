from sys import stdin
input = stdin.readline

N, M = map(int, input().rstrip().split())
lectures = list(map(int, input().rstrip().split()))

def count_blueray(mid):
  count = 1
  total = 0
  for lecture in lectures:
    if total + lecture > mid:
      count += 1
      total = lecture
    else:
      total += lecture
  return count

lo = max(lectures)
hi = sum(lectures)
result = hi
while lo <= hi:
  mid = (lo + hi) // 2
  if count_blueray(mid) <= M:
    result = mid
    hi = mid - 1
  else:
    lo = mid + 1

print(result)  