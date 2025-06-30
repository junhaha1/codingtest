def solution(sticker):
    dp = [[0] * len(sticker) for _ in range(2)]
    if len(sticker) <= 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker[0], sticker[1])
    else:   
        dp[1][1] = sticker[1]
        for i in range(len(sticker) - 1): #첫번째 선택했을 경우
            dp[0][i] = max(dp[0][i-1], dp[0][i-2] + sticker[i])    
        for i in range(1, len(sticker)): #두번째 선택했을 경우
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + sticker[i])

        return max(dp[0][len(sticker)-2], dp[1][len(sticker)-1])
    
    
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))