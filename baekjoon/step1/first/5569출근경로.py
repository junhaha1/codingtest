W, H = map(int, input().split())

dp = [[[[0, 0] for _ in range(2)] for _ in range(W)] for _ in range(H)]

dp[0][1][0][1] = 1
dp[1][0][1][1] = 1

for y in range(H):
    for x in range(W):
        for dir in range(2):
            for k in range(2):
                val = dp[y][x][dir][k]
                if val == 0: #연산할 필요가 없음. 해당 방향과 횟수로 방문하지 않은 것
                    continue

                dy, dx = (0, 1) if dir == 0 else (1, 0)
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W:
                    dp[ny][nx][dir][1] += val

                if k == 1: #연속 2칸 이동한 경우
                    new_dir = 0 if dir == 1 else 1
                    dy, dx = (0, 1) if new_dir == 0 else (1, 0)
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < H and 0 <= nx < W:
                        dp[ny][nx][new_dir][0] += val #횟수 초기화

MOD = 100000
ans = 0
for dir in range(2):
    for k in range(2):
        ans = (ans + dp[H-1][W-1][dir][k]) % MOD
print(ans)
