from sys import stdin

input = stdin.readline

N, S = map(int, input().split())

seq = list(map(int, input().split()))
prefix_sum = [0]

for s in seq:
    #초기 종료 조건1 : 수열의 목표값보다 크거나 같은 원소가 존재할 경우 중료
    if s >= S:
        print(1)
        exit()
    prefix_sum.append(prefix_sum[-1] + s)

#초기 종료 조건2 : 모든 수열의 합이 S보다 작으면 0 출력 후 종료
if prefix_sum[-1] < S:
    print(0)
    exit()

result = int(1e9)
left = 0
right = 0

while right <= N:
    temp = prefix_sum[right] - prefix_sum[left]
    if temp < S:
        right += 1
    else:
        result = min(result, right - left)
        left += 1

print(result if result != int(1e9) else 0)