from collections import defaultdict

def solution(commands):
    answer = []
    parent = [i for i in range(50 * 50)] #각 셀들의 부모 셀
    value = ["" for _ in range(50 * 50)] #각 셀들의 값
    group = defaultdict(set) #해당 셀(키값)을 부모로 가지는 셀(값)들을 저장
    
    for i in range(50 * 50):
        group[i].add(i)
    
    for command in commands:
        command = command.split()
        
        if command[0] == "UPDATE":
            if len(command[1:]) == 3:
                r, c, val = int(command[1]) - 1, int(command[2]) - 1, command[3]
                UPDATE1(r, c, val, parent, value)
                
            if len(command[1:]) == 2:
                val1, val2 = command[1], command[2]
                UPDATE2(val1, val2, value, parent)
                
        if command[0] == "MERGE":
            r1, c1 = int(command[1]) - 1, int(command[2]) - 1
            r2, c2 = int(command[3]) - 1, int(command[4]) - 1
            union(r1, c1, r2, c2, parent, value, group)
            
        if command[0] == "UNMERGE":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            UNMERGE(r, c, parent, value, group)
        
        if command[0] == "PRINT":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            idx = PRINT(r, c, parent)
            if value[idx] == "":
                answer.append("EMPTY")
            else:
                answer.append(value[idx])
    
    return answer

def UPDATE1(r, c, val, parent, value):
    idx = find(r * 50 + c, parent)
    value[idx] = val
    
def UPDATE2(val1, val2, value, parent):
    visited = set()
    for i in range(len(value)):
        root = find(i, parent)
        if root not in visited:
            visited.add(root)
            if value[root] == val1:
                value[root] = val2

def PRINT(r, c, parent):
    idx = find(r * 50 + c, parent)
    return idx

def UNMERGE(r, c, parent, value, group):
    target = r * 50 + c
    root = find(target, parent)
    cells = list(group[root])

    origin_value = value[root]  # 반드시 루트 기준
    
    for cell in cells: #root를 부모로 가진 셀들의 정보를 초기화
        parent[cell] = cell
        value[cell] = ""
        group[cell] = {cell}

    value[target] = origin_value  #셀 병합 해제의 기준이 된 셀의 값은 root의 값으로 변경
    

def union(r1, c1, r2, c2, parent, value, group):
    root1 = find(r1 * 50 + c1, parent)
    root2 = find(r2 * 50 + c2, parent)
    
    if root1 == root2:
        return  # 같은 셀이면 무시
    
    parent[root2] = root1
    
    group[root1] |= group[root2] #root1을 부모로 가지도록 root2를 가리키는 셀의 목록을 합침.
    del group[root2] #root2를 부모로 가지는 셀은 없어지므로 삭제
    
    if value[root1] == "" and value[root2] != "": #root1의 값이 없다면 root2의 값으로 갱신
        value[root1] = value[root2]
            
def find(idx, parent):
    if parent[idx] == idx:
        return idx
    
    parent[idx] = find(parent[idx], parent)
    return parent[idx]