x, y, w, s = map(int, input().split())

'''
블록 한칸 이동하는 시간
x좌표, y좌표 한번씩 : 2 * w 
대각선 : s
 
'''
if 2*w <= s: #블록 한칸 이동하는 시간이 대각선보다 작으므로 그냥 x,y좌표로만 이동
    print((x+y) * w)
else: #대각선 비용이 더 작은 경우, 대각선으로 갈 수 있을만큼 이동
    d = min(x, y)
    result = d * s
    rd = abs(x - y)
    if w > s:
        if rd % 2 == 0:
            result += rd * s
        else:
            result += (rd - 1) * s + w
    else:
        result += rd * w
    print(result)