from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

def count_k(n, k):
  count = 0
  t_k = k
  
  while t_k <= n:
    count += n // t_k
    t_k *= k
  
  return count
    
t_k = count_k(n, 2) - count_k(m, 2) - count_k(n - m, 2)
f_k = count_k(n, 5) - count_k(m, 5) - count_k(n - m, 5)

print(min(t_k, f_k))
  