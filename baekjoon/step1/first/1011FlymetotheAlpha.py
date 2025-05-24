for _ in range(int(input())):
    cur, END = map(int, input().split())
    distance = END - cur
    n = int(distance ** 0.5)
    
    if n ** 2 == distance:
        print(2*n-1)
    if n ** 2 < distance <= n ** 2 + n:
        print(2*n)
    if n ** 2 + n < distance < (n + 1) ** 2:
        print(2 * n + 1)
