from sys import stdin
input = stdin.readline

n = int(input().rstrip())

def gcf(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    print(a*b // gcf(a,b))