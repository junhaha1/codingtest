N = int(input())

sum_prime = [0, 2]
for i in range(3, N + 1):
    check = False
    for j in range(2, int((i ** 0.5)) + 1):
        if i % j == 0:
            check = True
            break
    if not check:
        sum_prime.append(sum_prime[-1] + i)

lp, rp = 0, 0
result = 0 
while rp < len(sum_prime):
    temp = sum_prime[rp] - sum_prime[lp]
    if temp == N:
        result += 1
        rp += 1
    elif temp < N:
        rp += 1
    elif temp > N:
        lp += 1

print(result)