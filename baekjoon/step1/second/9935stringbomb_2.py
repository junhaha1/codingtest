from sys import stdin

input = stdin.readline

words = list(input().rstrip())
bomb = input().rstrip()
bl = len(bomb)

stack = []

for w in words:
    stack.append(w)

    if len(stack) >= bl and ''.join(stack[-bl:]) == bomb:
        for _ in range(bl):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
