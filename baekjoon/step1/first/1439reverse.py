from sys import stdin

input = stdin.readline

num = input().rstrip()

cnt = 0

for i in range(len(num) - 1):
    if num[i] != num[i+1]:
        cnt += 1 

print((cnt+1)//2)
