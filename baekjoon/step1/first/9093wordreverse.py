from sys import stdin

input = stdin.readline

n = int(input())

for _ in range(n):
    words = input().rstrip().split()
    for w in words:
        w = list(w)
        w.reverse()
        print(''.join(w), end =" ")
    print()
