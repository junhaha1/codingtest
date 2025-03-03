from sys import stdin

input = stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

cnt = 0

def prime(a):
    for i in range(2, a//2 + 1):
        if a % i == 0:
            return 0
    return 1

for num in nums:
    if num == 1:
        continue
    cnt += prime(num)

print(cnt)