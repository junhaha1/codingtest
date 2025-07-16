def solution(matrix_sizes):
    N = len(matrix_sizes) #행렬의 갯수
    
    dp = [[0] * N for _ in range(N)]
    
    for length in range(2, N + 1): #구간의 길이
        for st in range(N - length + 1): #해당 구간 길이에서 만들 수 있는 행렬의 시작점
            ed = st + length - 1 #행렬의 끝점
            dp[st][ed] = int(1e9)
            
            for k in range(st, ed): #해당 구간에서 분할하는 위치
                value = matrix_sizes[st][0] * matrix_sizes[k][1] * matrix_sizes[ed][1] #해당 분할 위치를 통한 두 행렬의 곱 계산
                dp[st][ed] = min(dp[st][ed], 
                                dp[st][k] + dp[k + 1][ed] + value) #기존 앞선 행렬의 곱 횟수 + 현재 분할 위치를 통한 두 행렬의 곱 횟수

    return dp[0][-1]