# from collections import defaultdict, deque

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.money = 0
#         self.child = {}


# class Tree:
#     def __init__(self):
#         self.root = Node('-')
#         self.count = 0

#     def insert(self, parent, data):
#         if parent == '-':
#             self.root.child[data] = Node(data)
#         else:
#             parent_node = self.search_bfs(parent)
#             parent_node.child[data] = Node(data)

#     def search_bfs(self, data):
#         q = deque()
#         current_node = self.root
#         result_node = current_node
#         for ch in current_node.child.keys():
#             q.append(current_node.child[ch])
#         while q:
#             current_node = q.popleft()
#             if current_node.data == data:
#                 result_node = current_node
#                 break
#             for c in current_node.child.keys():
#                 q.append(current_node.child[c])

#         return result_node
#     # dfs 로 찾기

#     def search_data(self, data):
#         stack = []
#         current_node = self.root
#         result_node = current_node
#         for ch in current_node.child.keys():
#             stack.append(current_node.child[ch])
#         while stack:
#             current_node = stack.pop()
#             if current_node.data == data:
#                 result_node = current_node
#                 break
#             for c in current_node.child.keys():
#                 stack.append(current_node.child[c])

#         return result_node

#     def dfs_recursive(self, data, money):
#         self.__dfs_recursive(self.root, data, money)

#     def __dfs_recursive(self, node: Node, data, money):
#         result = 0
#         check = False
#         if node.data == data:
#             ten_percent = money // 10
#             node.money += (money - ten_percent)
#             return (True, ten_percent)
#         for ch in node.child.keys():
#             check, result = self.__dfs_recursive(node.child[ch], data, money)
#             if check == True:
#                 if result == 0:
#                     return (True, 0)
#                 else:
#                     break
#         if node == self.root:
#             node.money += result
#         else:
#             node.money += (result - (result//10))
#         return (check, result//10)

#     def bfs(self):
#         name_dict = dict()
#         q = deque()
#         q.append(self.root)
#         while q:
#             node = q.popleft()
#             for ch in node.child.keys():
#                 name_dict[ch] = node.child[ch].money
#                 q.append(node.child[ch])
#         return name_dict


# def solution(enroll, referral, seller, amount):
#     answer = []
#     tree = Tree()
#     for i, en in enumerate(enroll):
#         tree.insert(referral[i], en)
#     for j, sell in enumerate(seller):
#         if amount[j] > 0:
#             tree.dfs_recursive(sell, amount[j]*100)
#     tmp = tree.bfs()
#     for en in enroll:
#         answer.append(tmp[en])

#     return answer


def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    idx_list = {}
    for idx, name in enumerate(enroll):
        idx_list[name] = idx
    for idx, name in enumerate(seller):
        price = 100*amount[idx]
        answer[idx_list[name]] += price
        while referral[idx_list[name]] != "-":
            answer[idx_list[name]] -= price//10
            name = referral[idx_list[name]]
            answer[idx_list[name]] += price//10
            price = price//10
            if price == 0:
                break
        answer[idx_list[name]] -= price//10
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary",
      "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]) == [360, 958, 108, 0, 450, 18, 180, 1080])
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary",
      "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]) == [0, 110, 378, 180, 270, 450, 0, 0])
