from sys import stdin

alphas = stdin.readline().rstrip()
ap = [-1] * 26

for i in range(len(alphas)):
  if ap[ord(alphas[i]) - ord('a')] == -1:
    ap[ord(alphas[i]) - ord('a')] = i
    
print(*ap)