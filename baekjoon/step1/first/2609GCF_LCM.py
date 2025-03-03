n, m = map(int, input().split())

if n < m:
    t = n
    n = m
    m = t

n1= n
m1 = m
while True:
    r = n1 % m1
    if r == 0:
        break
    n1 = m1
    m1 = r

print(m1) #최대 공약수
print(int((n*m)/m1))#최소 공배수