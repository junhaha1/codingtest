from sys import stdin

input = stdin.readline

while True:
    st = input().rstrip('\n')
    if st == '':
        break
    ls, us, nm, sp = 0, 0, 0, 0
    for s in st:
        if s.islower(): ls += 1
        elif s.isupper(): us += 1
        elif s.isdecimal(): nm += 1
        elif s.isspace(): sp += 1

    print(ls, us, nm, sp, sep=' ')