#단순 연결 리스트 : 단순 연결 리스트는 헤더 노드가 존재하며 
#헤더 노드는 다음 노드를 그리고 다음 노드는 그 다음 노드를 가리킨다. 
#한 방향으로 연결되어 단순 연결 리스트라고 부른다.

class Node:
    def __init__(self,item):
        self.data = item # data
        self.next = None # next link (다음 인자를 가리킴)
        
# next 는 다음 노드에 접근하는 방법입니다 
# 포인터로 접근 
# head = Node(5)
# next_node = Node(12)
# head.next = next_node

class SignleLinkedList:
    def __init__(self,item):
        self.head = Node(item)
        self.list_size = 1
    
    def __str__(self):
        print_list = '['
        node = self.head
        while True:
            print_list += str(node.data)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list
    
    def insertFirst(self,data):
        temp_node = self.head  # 기존 헤드를 잠시 보관 
        self.head = Node(data) # 헤드를 새로운 노드로 변경 
        self.head.next = temp_node # 새로 생성된 헤드의 링크를 기존 헤드의 링크로 변경 
        self.list_size += 1
    
    def insertLast(self,data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next
        new_node = Node(data)
        node.next  = new_node 
        self.list_size += 1
    def insertIndex(self,num,data):
        if self.head.next == None:
            self.insertLast(data)
            return 
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        temp_node = node.next
        new_node = Node(data)
        node.next = new_node 
        new_node.next = temp_node
        self.list_size += 1
     
    def selectNode(self,index):
        if index > self.list_size:
            return 'Overflow'
        node = self.head;
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node
        
    def indexOf(self,index):
        if index > self.list_size:
            return 'Overflow'
        node = self.head;
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node.data
    
    def deleteNode(self,num):
        if self.list_size < 1:
            return 
        elif self.list_size < num:
            return 

        node = self.selectNode(num-1)
        print(node.data)
        node.next = node.next.next
        
    def size(self):
        return str(self.list_size)
    

if __name__ == "__main__":
    m_list = SignleLinkedList(1)
    m_list.insertFirst(5)
    m_list.insertFirst(6)
    m_list.insertLast(10)
    print('LinkedList : ',m_list)
    print('LinkedList size: ',m_list.size())
    print('LinkedList index :',3,'=>',m_list.indexOf(3))
    print('LinkedList index :',10,'=>',m_list.indexOf(10))
    m_list.insertIndex(2,3)
    print('LinkedList : ',m_list)
    print('delete')
    m_list.deleteNode(3)
    print('LinkedList : ',m_list)
    
    
