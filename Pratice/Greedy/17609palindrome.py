from sys import stdin
input = stdin.readline

t = int(input())

result = []

def twop(left, right):
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else: #서로 다른 경우
            if right - 1 > left: #왼쪽으로
                temp = word[:right-1] + word[right+1:]
                if temp[:] == temp[::-1]:
                    return 1
            if left + 1 < right: #오른쪽으로
                temp = word[:left] + word[left+1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0
        
for _ in range(t):
    word = input()
    
    left = 0
    right = len(word) - 1
    
    result.append(twop(left, right))
    
for r in result:
    print(r)