from collections import deque
from copy import copy
<<<<<<< HEAD
from locale import currency


def solution(n:int, k:int, cmd: list[str]):
    answer = ''
    chart = [i for i in range(n)]
    point = k
    temp_db = copy(chart)
    # 휴지통 배열
    rebin_cycle = []
    cmd_q = deque(cmd)
    while cmd_q:
        c = cmd_q.popleft()
        if c[0] == 'D':
            point = min(len(temp_db)-1,point+int(c[-1]))
        elif c[0] == 'U':
            point = max(0,point-int(c[-1]))
        elif c[0] == 'C':
            rebin_cycle.append(temp_db.pop(point))
        elif c[0] == 'Z':
            if len(rebin_cycle) > 0:
                tmp_point = rebin_cycle.pop()
                if tmp_point >= len(temp_db):
                    temp_db.append(tmp_point)
                else:
                    temp_db.insert(tmp_point,tmp_point)
    check = 0                
    for s in temp_db:
        if check == s:
            answer += 'O'
            check += 1
        else:
            answer += 'X'*int(s-check) + 'O'
            check = s+1
    else:
        if check < n:
            answer +='O'*int(len(n)-check)
    #print(answer)
    return answer
    
    
    

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])=="OOOOXOOO")
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])=="OOXOXOOO")
=======


def solution(n, k, cmd):
    answer = ''

    return answer


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.next = None


class LinkList:
    def __init__(self, n):
        self.head = Node(None)
        self.deleted = []
        self.answer = ['O' for _ in range(n)]

        #  while cmd_q:
        #         c = cmd_q.popleft()
        #         if c[0] == 'D':
        #             point = min(len(temp_db)-1, point+int(c[-1]))
        #         elif c[0] == 'U':
        #             point = max(0, point-int(c[-1]))
        #         elif c[0] == 'C':
        #             rebin_cycle.append(temp_db.pop(point))
        #         elif c[0] == 'Z':
        #             if len(rebin_cycle) > 0:
        #                 tmp_point = rebin_cycle.pop()
        #                 if tmp_point >= len(temp_db):
        #                     temp_db.append(tmp_point)
        #                 else:
        #                     temp_db.insert(tmp_point, tmp_point)
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
        #             answer += 'O'*int(len(n)-check)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))


# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
#         self.next = None

# class LinkedList:
#     def __init__(self, n):
#         self.head = Node(None)
#         self.deleted = []
#         self.answer = ['O' for _ in range(n)]

#     def append(self, data):
#         node = self.head
#         while node.next:
#             node = node.next
#         else:
#             node.next = Node(data)


#     def printall(self):
#         node = self.head
#         arr = [node.data]
#         while node.next:
#             node = node.next
#             arr.append(node.data)


#     def delete(self, ind):
#         node = self.head
#         answer = ind
#         while ind:
#             node = node.next
#             ind -= 1
#         else:
#             deleting = node.next
#             self.answer[deleting.data] = 'X'
#             self.deleted.append(deleting)
#             node.next = deleting.next
#         return answer - 1 if not(deleting.next) else answer

#     def restore(self):
#         lastone = self.deleted.pop()
#         self.answer[lastone.data] = 'O'
#         node = self.head
#         while node.next and node.next.data != lastone.next.data:
#             node = node.next
#         else:
#             nextone = node.next
#             node.next = lastone
#             node.next.next = nextone

#     def getanswer(self):
#         return self.answer


# def solution(n, k, command):
#     link = LinkedList(n)
#     for ind in range(n):
#         link.append(ind)
#     else:
#         link.append(None)

#     for cmd in command:
#         if len(cmd) > 1: # move
#             act, num = cmd.split(' ')
#             if act == 'D':
#                 k += int(num)
#             else:
#                 k -= int(num)
#         else:
#             if cmd == 'C':
#                 k = link.delete(k)
#             else:
#                 link.restore()


#     return ''.join(link.answer)
>>>>>>> 9415c27a123fff434f91d3b6dec726664647c40e
