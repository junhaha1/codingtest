from sys import stdin

input = stdin.readline

def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return
    print(n)

s, e = map(int, input().rstrip().split())
for num in range(s, e + 1):
    if num == 1: continue # 1은 제외하기
    prime(num)