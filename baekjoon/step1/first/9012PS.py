from sys import stdin

n = int(input())


for _ in range(n):
    stack = []
    cnt = 0
    string = input().rstrip()
    for w in string:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                cnt += 1
        
    if cnt > 0 or len(stack) > 0:
        print("NO")
    else:
        print("YES")