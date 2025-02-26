from sys import stdin

n = int(input())
string = list(input().rstrip())
num = [0] * n
for i in range(n):
    num[i] = int(input())
    
stack = []

for i in string:
    if 'A'<= i <= 'Z':
        stack.append(num[ord(i) - 65])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+': stack.append(a + b)
        if i == '-': stack.append(a - b)
        if i == '*': stack.append(a * b)
        if i == '/': stack.append(a/b)

    
print("%.2f" % stack[0])