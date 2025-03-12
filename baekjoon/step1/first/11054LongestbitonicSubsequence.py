from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
r_a = a[::-1]

dp1 = [1] * n #증가하는
dp2 = [1] * n #감소하는

def bs(a, lis):
  s = 0
  e = len(lis) - 1
  while s <= e:
    m = (s + e) // 2
    if a > lis[m]:
      s = m + 1
    else:
      e = m - 1
  return s
  
i_lis = [a[0]]
d_lis = [r_a[0]]

for i in range(1, n):
  if i_lis[-1] < a[i]:
    i_lis.append(a[i])
    dp1[i] = len(i_lis)
  else:
    idx = bs(a[i], i_lis)
    i_lis[idx] = a[i]
    dp1[i] = len(i_lis[:idx + 1])
  if d_lis[-1] < r_a[i]:
    d_lis.append(r_a[i])
    dp2[i] = len(d_lis)
  else:
    idx = bs(r_a[i], d_lis)
    d_lis[idx] = r_a[i]
    dp2[i] = len(d_lis[:idx + 1])

result = 0
for i in range(n):
  result = max(result, dp1[i] + dp2[-i-1] - 1)
print(result)