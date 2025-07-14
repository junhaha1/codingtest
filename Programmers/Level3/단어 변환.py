from collections import defaultdict, deque
def solution(begin, target, words):
    words.append(begin)
    
    graph = defaultdict(list)
    depth = dict()
    
    for word1 in words:
        for word2 in words:
            if word1 != word2 and word2 not in graph[word1]:
                if str_check(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
                    depth[word1] = -1
                    depth[word2] = -1
    q = deque()
    depth[begin] = 0
    q.append(begin)
    
    while q:
        word = q.popleft()
        for child in graph[word]:
            if depth[child] == -1: #아직 방문하지 않은 단어일 경우
                depth[child] = depth[word] + 1
                q.append(child)
    
    if target not in depth:
        return 0
    else:
        return depth[target]
    

def str_check(str1, str2):
    count = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            count += 1
    return True if count == 1 else False