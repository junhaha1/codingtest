from sys import stdin

input = stdin.readline

n = int(input())

cnt = 1
stack = []
result = []
for _ in range(n):
    num = int(input())

    while num >= cnt:
        stack.append(cnt) #PUSH
        cnt += 1
        result.append('+')
    
    if stack[-1] == num: #스택 마지막 값이 입력받은 값과 같다면 pop
        stack.pop()
        result.append('-')
    else:
        result = ['NO']
        break

for s in result:
    print(s)