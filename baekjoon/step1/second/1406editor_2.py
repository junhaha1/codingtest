from sys import stdin

input = stdin.readline

left = list(input().rstrip())
right = []

n = int(input().rstrip()) #명령어 갯수

for _ in range(n):
    c = input().rstrip() 
    if left and c == 'L': #커서를 왼쪽으로
        right.append(left.pop())
    elif right and c == 'D': #커서를 오른쪽으로
        left.append(right.pop())
    elif left and c == 'B': #커서 왼쪽에 있는 문자 삭제
        left.pop()
    elif c[0] == 'P': #P $입력 시에 left에 입력 추가
        c, w = c.split()
        left.append(w)

print(''.join(left + right[::-1]))