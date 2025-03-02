from sys import stdin

words = stdin.readline().rstrip()

alpha = [0] * 26


for w in words:
    alpha[ord(w) - ord('a')] += 1

print(*alpha)