from locale import currency


class Node(object):
    def __init__(self,data= None,index = None):
        self.data = data
        self.prev = None
        self.next = None
        self.index = index
    
class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.list_size = 1
        
    def __str__(self):
        s = '' 
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.data != None:
                s += current_node.data
            if current_node.next == self.head:
                break
        return s
      
    def insertLast(self,data,index):   
        new_node = Node(data,index)
        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head

        if not self.head.prev == None:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
        self.head.prev = new_node
        new_node.next = self.head
        self.list_size += 1    

    def insertMiddleBefore(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data,num)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.list_size += 1   
        
    def insertMiddleAfter(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.list_size += 1
    
    def selectNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size <= num:
            return # Overflow
        count = 0
        node = self.head
        if int(self.list_size/2) > num:
            while count < num:
                node = node.next
                count += 1
        else:
            repeat = self.list_size - num
            while count < repeat:
                node = node.prev
                count += 1
        return node
    
    def answer_print(self,n):
        s = '' 
        current_node = self.head
        count = 0
        while count <= n:
            if current_node.index != None:
                if current_node.index == count:
                    s += current_node.data
                    current_node = current_node.next
                else:
                    count += 1
            else:
                s += 'X'
            if current_node.next == self.head:
                break
            
        return s
    
    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size <= num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num)
        node.prev.next = node.next
        node.next.prev = node.prev
        # del node 
        

def solution(n:int, k:int, cmd: list[str]):
    answer = []
    # Linked List 를 이용하여 풀기 
    linked_list = LinkedList()
    for i in range(n):
        linked_list.insertLast('O',i)
#     "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
    stack_delete = []
    point = k
    for c in cmd:
        print('cmd' , c)
        if c[0] in ['U','D']:
            c,move = c.split(' ')
            if c == 'U':
                point = max(0,abs(point-int(move)))
            elif c == 'D':
                point = min(n-1,abs(point+int(move)))    
        elif c == 'C':
            linked_list.deleteNode(point)
            stack_delete.append(point)
        elif c == 'Z':
            delete_point = stack_delete.pop()
            linked_list.insertMiddleBefore(delete_point,'O')
    print(linked_list)
    answer = linked_list.answer_print(n)
    print(answer)
    return answer
    
    
  
    
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