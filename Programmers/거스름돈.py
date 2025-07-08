def solution(n, money):
    MOD = 1_000_000_007
    dp = [1] + [0] * n
    for m in money:
        for i in range(m, n + 1):
            dp[i] = (dp[i] + dp[i - m]) % MOD
    return dp[n] 