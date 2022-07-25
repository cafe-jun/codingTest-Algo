class LinkedList:
    class Node:
        def __init__(self, num, prev):
            self.num = num
            self.prev = prev
            self.next = None

    def __init__(self, num, start):
        self.root = self.Node(0, None)
        self.current = None
        self.stack = []
        temp = self.root
        for i in range(1, num):
            new_node = self.Node(i, temp)
            temp.next = new_node
            if i == start:
                self.current = new_node
            temp = new_node

    def up(self, num):
        for _ in range(num):
            if self.current.prev:
                self.current = self.current.prev

    def down(self, num):
        for _ in range(num):
            if self.current.next:
                self.current = self.current.next

    def remove(self):
        remove_node = self.current
        self.stack.append(remove_node)
        if remove_node.next:
            if remove_node == self.root:
                self.root = remove_node.next
            self.current = remove_node.next
            self.current.prev = remove_node.prev
            if remove_node.prev:
                remove_node.prev.next = self.current
        else:
            self.current = remove_node.prev
            self.current.next = None

    def recover(self):
        recover_node = self.stack.pop()
        if recover_node.prev:
            recover_node.prev.next = recover_node
        if recover_node.next:
            recover_node.next.prev = recover_node
            if recover_node.next == self.root:
                self.root = recover_node

    def get_root(self):
        return self.root

    def __bool__(self):
        return True


def solution(n, k, cmd):
    table = LinkedList(n, k)
    for c in cmd:
        if c[0] == 'U':
            table.up(int(c.split()[1]))
        elif c[0] == 'D':
            table.down(int(c.split()[1]))
        elif c[0] == 'C':
            table.remove()
        else:
            table.recover()
    node = table.get_root()
    result = ["X"] * n
    while node:
        result[node.num] = "O"
        node = node.next
    return "".join(result)
# class Node(object):
#     def __init__(self, data=None, index=None):
#         self.data = data
#         self.prev = None
#         self.next = None
#         self.index = index


# class LinkedList(object):
#     def __init__(self):
#         self.head = Node(None)
#         self.list_size = 1

#     def __str__(self):
#         s = ''
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#             if current_node.data != None:
#                 s += current_node.data
#             if current_node.next == self.head:
#                 break
#         return s

#     def insertLast(self, data, index):
#         new_node = Node(data, index)
#         if self.head.next == None:
#             self.head.next = new_node
#             new_node.prev = self.head

#         if not self.head.prev == None:
#             self.head.prev.next = new_node
#             new_node.prev = self.head.prev
#         self.head.prev = new_node
#         new_node.next = self.head
#         self.list_size += 1

#     def insertMiddleBefore(self, num, data):
#         node = self.selectNode(num)
#         new_node = Node(data, num)
#         new_node.prev = node.prev
#         new_node.next = node
#         node.prev.next = new_node
#         node.prev = new_node
#         self.list_size += 1

#     def insertMiddleAfter(self, num, data):
#         node = self.selectNode(num)
#         new_node = Node(data)
#         new_node.prev = node
#         new_node.next = node.next
#         node.next.prev = new_node
#         node.next = new_node
#         self.list_size += 1

#     def selectNode(self, num):
#         if self.list_size < 1:
#             return  # Underflow
#         elif self.list_size <= num:
#             return  # Overflow
#         count = 0
#         node = self.head
#         if int(self.list_size/2) > num:
#             while count <= num:
#                 node = node.next
#                 count += 1
#         else:
#             repeat = self.list_size - num
#             while count <= repeat:
#                 node = node.prev
#                 count += 1
#         print(node.index)
#         return node

#     def answer_print(self, n):
#         s = ''
#         current_node = self.head
#         count = 1
#         while count <= n:
#             if current_node.next == self.head:
#                 break
#             current_node = current_node.next
#             if current_node.index != None:
#                 if current_node.index == count:
#                     s += current_node.data
#                     current_node = current_node.next
#                 else:
#                     count += 1
#             else:
#                 s += 'X'

#         return s

#     def deleteNode(self, num):
#         if self.list_size < 1:
#             return  # Underflow
#         elif self.list_size <= num:
#             return  # Overflow

#         if num == 0:
#             self.deleteHead()
#             return
#         node = self.selectNode(num - 1)
#         node.next = node.next.next
#         del_node = node.next
#         del del_node

#     def deleteHead(self):
#         node = self.head
#         self.head = node.next
#         del node


def solution(n: int, k: int, cmd: list[str]):
    answer = []
    # Linked List 를 이용하여 풀기
    linked_list = LinkedList()
    for i in range(n):
        linked_list.insertLast('O', i)
    stack_delete = []
    point = k
    for c in cmd:
        print('cmd', c)
        if c[0] in ['U', 'D']:
            c, move = c.split(' ')
            if c == 'U':
                point = max(0, abs(point-int(move)))
            elif c == 'D':
                point = min(n-1, abs(point+int(move)))
        elif c == 'C':
            linked_list.deleteNode(point)
            stack_delete.append(point)
        elif c == 'Z':
            if len(stack_delete) > 0:
                delete_point = stack_delete.pop()
                linked_list.insertMiddleBefore(delete_point, 'O')
    print(linked_list)
    answer = linked_list.answer_print(n)
    print(answer)
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z"]) == "OOOOXOOO")
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
