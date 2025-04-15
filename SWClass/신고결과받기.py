def solution(id_list, report, k):
     answer = [0] * (len(id_list))

     board = [[0] * (len(id_list)) for _ in range(len(id_list))]
     for i in range(len(report)):
          user1, user2 = report[i].split()
          board[id_list.index(user1)][id_list.index(user2)] = 1
          
     for c in range(len(id_list)):
          cnt = 0
          for r in range(len(id_list)):
               cnt += board[r][c]
               if cnt >= k:
                    for r2 in range(len(id_list)):
                         answer[r2] += board[r2][c]
                    break

     return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))