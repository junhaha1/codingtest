from sys import stdin
input = stdin.readline

words = '' #단어들 담는 곳
word = input().rstrip()
check = False
result = ''
for w in word:
    if w == '<':
        check = True
        result += words[::-1] + '<'
        words = ''
        continue
    if w == '>':
        check = False
        result += '>'
        continue
    if check:
        result += w
    else:
        if w == ' ':
            result += words[::-1] + ' '
            words = ''
        else:
            words += w

result += words[::-1]

print(result)
