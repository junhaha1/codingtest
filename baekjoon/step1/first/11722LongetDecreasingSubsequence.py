from sys import stdin

input = stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

dp = [0] * 1001

