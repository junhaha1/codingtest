from sys import stdin
input = stdin.readline

n, m = map(int, input().rstrip().split())

def find_k(a, b):
    cnt = 0
    #n // 2의 뜻은 n이하의 수를 2를 이용하여 만들 수 있는 갯수라는 의미
    tk = b
    while tk <= a:
        cnt += a // tk
        tk *= b
    return cnt

two = find_k(n, 2) - (find_k(n-m, 2) + find_k(m, 2))
five = find_k(n, 5) - (find_k(n-m, 5) + find_k(m, 5))

print(min(two, five))