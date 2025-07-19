def solution(n):
    l = n
    r = n
    
    answer = dfs(l, r)
    
    return answer
    
def dfs(l, r):
    if l == 0 and r == 0:
        return 1
    count = 0
    if l != 0:
        count += dfs(l - 1, r)
    if l < r:
        count += dfs(l, r - 1)
    
    return count