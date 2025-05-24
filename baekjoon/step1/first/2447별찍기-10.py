N = int(input())

def dfs(n):
    if n == 1:
        return '*'

    stars = dfs(n//3)
    result = []
    
    for star in stars:
        result.append(star * 3)
    for star in stars:
        result.append(star + ' ' * (n // 3) + star)
    for star in stars:
        result.append(star * 3)
    print(result)
    return result

print(*dfs(N), sep='\n')
