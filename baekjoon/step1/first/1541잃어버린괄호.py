temp = input()
result = 0

num = []
num_t = 0
i = 1

#입력받은 문자열을 파악하여 숫자로 만듬. 
for t in temp:
    if t != '+' and t != '-': #연산자를 만나기 전까지 숫자 만들기
        num_t *= 10
        num_t += int(t)
    else: #연산자를 만났을 경우 만들어둔 숫자 추가하기 
        num.append(num_t * i)
        if t == '-': #만약 t가 -라면 이때부터 모든 숫자는 음수로 변경
            i = -1
        num_t = 0
num.append(num_t * i)

print(sum(num))
