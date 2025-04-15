def solution(id_list, report, k):
     answer = [0] * (len(id_list) + 1)

     board = [[0] * (len(id_list) + 1) for _ in range(len(id_list) + 1)]
     for i in range(len(report)):
          user1, user2 = report[i].split()
          board[id_list.index(user1) + 1][id_list.index(user2) + 1] = 1
          
     for c in range(1, len(id_list) + 1):
          cnt = 0
          for r in range(1, len(id_list) + 1):
               cnt += board[r][c]
               if cnt >= k:
                    for r2 in range(1, len(id_list) + 1):
                         answer[r2] += board[c][r2]
                    break

     print(*board, sep="\n")
     print()
     print(answer)
     return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)