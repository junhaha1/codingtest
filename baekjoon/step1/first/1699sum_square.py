from sys import stdin

input = stdin.readline

n = int(input())

dp = [0] + [i for i in range(1, n + 1)] #각 n에 대하여 1^2으로 만들었을 경우를 초기값으로 설정해둠. 

#점화식
#dp[i] = min(dp[i], dp[i - (j**2)] + 1) => 1을 더해주는 건 j**2의 제곱수 합 갯수는 1로 고정되어있음.
#그럼 dp[j*j]를 더해주면 되지않냐? 예를 들어 4같은 경우 dp[j*j]를 더한다면 dp[4]를 초기화하는 과정에 dp[4]를 더한다면 1이 아닌 다른 값을 더할 수도 있기 때문에 1로 고정하여 더해줌. 

for i in range(2, n + 1):
    j = 1
    while j ** 2 <= i:
        dp[i] = min(dp[i], dp[i - (j**2)] + 1)
        j += 1

print(dp[n])