import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b

for _ in range(m):
    op, n1, n2 = map(int, input().split())

    if op == 0: #합집합 연산
        union(n1, n2)
    if op == 1: #같은 집합인지 확인
        if find(n1) == find(n2):
            print("YES")
        else:
            print("NO")
    # print(parent) #로그 출력용
    # print()