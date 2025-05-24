N = int(input())

def draw_tri(n):
    if n == 3:
        return ["  *  ",
                " * * ",
                "*****"]
    
    stars = draw_tri(n//2)
    triangle = []
    for star in stars:
        triangle.append(' ' * (n//2) + star + ' ' * (n//2))
    for star in stars:
        triangle.append(star + ' ' + star)

    return triangle

print(*draw_tri(N), sep='\n')
