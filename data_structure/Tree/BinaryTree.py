class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

# 전위 순회
# D : 현재 노드를 출력한다
# L : 현재 노드 왼쪽 서브트리로 이동한다
# R : 현재 노드 오른쪽 서브트리로 이동한다

# 중위 순회


# 후위 순회


class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left == None:
            self.preorderTraversal(node.left)
        if not node.right == None:
            self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left == None:
            self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None:
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left == None:
            self.postorderTraversal(node.left)
        if not node.right == None:
            self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node


if __name__ == "__main__":
    node = []
    node.append(Node('-'))
    node.append(Node('*'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    m_tree = Tree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i], node[i*2+1], node[i*2+2])
    print('전위 순회:')
    m_tree.preorderTraversal(m_tree.root)
    print('')
    print('중위 순회:')
    m_tree.inorderTraversal(m_tree.root)
    print('')
    print('후위 순회:')
    m_tree.postorderTraversal(m_tree.root)
