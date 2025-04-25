N = int(input())

queens = [-1] * N

def is_possible(r):
    for row in range(r):
        if queens[row] == queens[r]:
            return False
        if (r - row) == abs(queens[row] - queens[r]):
            return False
    return True

def dfs(row):
    if row == N:
        return 1
    
    ans = 0
    for i in range(N):
        queens[row] = i
        if is_possible(row):
            ans += dfs(row + 1)
    return ans

print(dfs(0))