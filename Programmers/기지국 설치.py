def solution(n, stations, w):
    answer = 0
    
    width = w * 2 + 1
    prev = 1
    for stat in stations:
        s = stat - w - 1
        if s >= 1:
            answer += (s - prev) // width + 1
        prev = stat + w + 1
    
    #print(prev, n)
    if prev <= n:
        answer += (n - prev) // width + 1
    
    return answer