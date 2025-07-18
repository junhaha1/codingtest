def solution(n, t, m, timetable):
    times = []
    bus = []
    bus_t = 540 #버스 출발 시간
    
    for time in timetable:
        hh, mm = map(int, time.split(':'))
        times.append(hh * 60 + mm)
        
    times.sort()
    
    for i in range(n):
        tmp = []
        for time in times:
            if len(tmp) < m and time <= bus_t:
                tmp.append(time)
        bus.append(tmp)
        times = times[len(tmp):]
        if i != n - 1:
            bus_t += t
    
    if len(bus[-1]) < m: #마지막 버스가 꽉 차지 않은 경우
        late_time = bus_t
    else: #마지막 버스가 꽉 찬 경우
        late_time = bus[-1][-1] - 1   
    
    return scale_time(late_time)

def scale_time(val):
    h = str(val // 60)
    s = str(val % 60)
    
    if len(h) == 1:
        h = '0' + h
    if len(s) == 1:
        s = '0' + s
    return h + ':' + s