from sys import stdin
from collections import deque

input = stdin.readline
k = int(input())

w, h = map(int, input().rstrip().split())

board = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

def bfs(s):
    q = deque()
    
    