from collections import deque
from math import ceil
t = int(input())

for i in range(t):
    beer = 20 #맥주
    empty_beer = 0 #다 먹은 맥주
    n = int(input()) #편의점 갯수
    
    hx, hy = map(int, input().split()) #집 좌표
    markets = []
    for j in range(n): #편의점 좌표 추가
        markets.append(tuple(map(int, input().split())))
    fx, fy = map(int, input().split())
    
    board = [[0 for _ in range(fx)] for _ in range(fy)]
    
    min_beer = ceil((fx + fy) / 50)
    visit_number = ceil(min_beer / 20) -1 #편의점 방문 해야하는 최소 횟수
    print(min_beer, visit_number)
    print("test")