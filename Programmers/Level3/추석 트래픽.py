def solution(lines):
    answer = 0
    seconds = []
    
    if len(lines) == 1: #1개인 경우 제외
        return 1
    
    for line in lines:
        _, time, s = line.split()
        hh, mm, ee = map(float, time.split(':'))
        mm += hh * 60
        ee += mm * 60
        ss = round(ee - float(s[:-1]), 3) + 0.001
        seconds.append((ss, ee))
        
    #마지막 로그 종료 시간 - 첫번째 로그 시작 시간
    total_second = int(seconds[-1][1]) - int(seconds[0][0])
    
    for i, second in enumerate(seconds):
        _, end = second
        tmp = 1
        for start, _ in seconds[i + 1:]:
            if start < end + 1:
                tmp += 1
        answer = max(answer, tmp)
        
    return answer