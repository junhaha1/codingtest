from sys import stdin

input = stdin.readline

print(oct(int(input().rstrip(), 2))[2:])