from collections import deque



def solution(n:int, k:int, cmd: list[str]):
    answer = []
    node1 = Node(5)
    node2 = Node(2)
    node1.next = node2 
    head = node1 
    print(node1.data)
    print(node2.data)
    # Linked List 를 이용하여 풀기 
    return answer
    
    
class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class LinkedList(object):
    def __init__(self):
        pass
    
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])=="OOOOXOOO")
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])=="OOXOXOOO")



#   answer = ''
#     chart = [i for i in range(n)]
#     point = k
#     temp_db = copy(chart)
#     # 휴지통 배열
#     rebin_cycle = []
#     cmd_q = deque(cmd)
#     while cmd_q:
#         c = cmd_q.popleft()
#         if c[0] == 'D':
#             point = min(len(temp_db)-1,point+int(c[-1]))
#         elif c[0] == 'U':
#             point = max(0,point-int(c[-1]))
#         elif c[0] == 'C':
#             rebin_cycle.append(temp_db.pop(point))
#         elif c[0] == 'Z':
#             if len(rebin_cycle) > 0:
#                 tmp_point = rebin_cycle.pop()
#                 if tmp_point >= len(temp_db):
#                     temp_db.append(tmp_point)
#                 else:
#                     temp_db.insert(tmp_point,tmp_point)
#     check = 0                
#     for s in temp_db:
#         if check == s:
#             answer += 'O'
#             check += 1
#         else:
#             answer += 'X'*int(s-check) + 'O'
#             check = s+1
#     else:
#         if check < n:
#             answer +='O'*int(len(n)-check)
#     #print(answer)