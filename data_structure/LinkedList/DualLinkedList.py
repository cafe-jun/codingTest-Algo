


class Node(object):
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DualLinkedList(object):
    def __init__(self,data):
        self.head = Node(data)
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
        node = self.head
        new_node = Node(data)
        self.head = new_node
        new_node.next = node
        node.prev = new_node
            
    def selectNode(self,num):
        
    

if __name__ == '__main__':
    d_list = DualLinkedList(5)
    d_list.insertFirst(3)
    d_list.insertFirst(2)
    d_list.insertFirst(1)
    print('DualLinkedList :',d_list)