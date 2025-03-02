from sys import stdin

exp = stdin.readline().rstrip()

result = ''

op = []
pt = {'(':0, '*':1, '/' : 1, '+':2, '-':2} #우선순위 미리 저장

for e in exp:
    if 'A' <= e <= 'Z': #피연자일 경우
        result += e
    else: #연산자일 경우
        if len(op) == 0: #스택이 비었을 땐 일단 push
            op.append(e)
        else: #스택이 비어있지 않을 때
            if e == ')': #')'일 경우 '('를 만날 때까지 모든 연산자 POP
                t = op.pop()
                while t != '(':
                    result += t
                    t = op.pop()
            else: #')'가 아닐 경우
                if op[-1] == '(' or pt[op[-1]] > pt[e]: #push 연산
                    op.append(e)
                else: #pop연산 후 push연산
                    while op and op[-1] != '(' and pt[op[-1]] <= pt[e]: 
                        result += op.pop()
                    op.append(e)
while len(op) > 0:
    result += op.pop()

print(result)