#silver2
from sys import stdin
import math

input = stdin.readline

n = int(input().rstrip())

era = [False, False] + [True] * (1000000 - 1) #총 1000001개

for i in range(2, 1000001):
    for j in range(2*i, 1000001, i):
        era[j] = False

for _ in range(n):
    num = int(input().rstrip())
    cnt = 0
    s = set()
    for i in range(2, num):
        if era[i] and era[num-i]:
            s.add(abs(num-i-i))
    print(len(s))