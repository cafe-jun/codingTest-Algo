# # 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
# # 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
# # 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
# # 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

import bisect
import itertools
import collections


def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)])
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l, _, p, _, c, _, f, point = q.split()
        key = ''.join([l, p, c, f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers

# class Node(object):
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.score = []
#         self.children = {}
#         self.depth = 0
#         self.count = 0


# class Trie:
#     result: dict

#     def __init__(self):
#         self.head = Node(None)
#         self.result = {}
#         self.count = 0

#     def tree_setting(self, idx, setting, node):
#         if node == None:
#             current_node = self.head
#         else:
#             current_node = node
#         if current_node.depth == idx:
#             for s in setting:
#                 current_node.children[s] = Node(s)
#                 current_node.children[s].depth += current_node.depth+1
#         else:
#             for k in current_node.children.keys():
#                 self.tree_setting(idx, setting, current_node.children[k])

#     def insert(self, data_list):
#         current_node = self.head
#         self.count += 1
#         for data in data_list[:-1]:
#             tmp_node = current_node.children['-']
#             for t in tmp_node.children.keys():
#                 tmp_node.score.append(data_list[-1])
#             current_node = current_node.children[data]
#             current_node.count += 1
#             current_node.data = data
#             current_node.score.append(data_list[-1])

#     def get_score(self, querys, query, idx, node):
#         result = 0
#         current_node = node
#         if idx == 4:
#             count = 0
#             for s in sorted(current_node.score, reverse=True):
#                 if int(query) <= int(s):
#                     count += 1
#                 else:
#                     break
#             return count
#         if query in current_node.children:
#             result += self.get_score(
#                 querys, querys[idx+1], idx+1, current_node.children[query])
#         # elif query == '-':
#         #     for k in current_node.children.keys():
#         #         result += self.get_score(
#         #             querys, querys[idx+1], idx+1, current_node.children[k])
#         return result

#     def search_count(self, querys):
#         result = 0
#         current_node = self.head
#         result = self.get_score(querys, querys[0], 0, current_node)
#         return result


# def solution(info, query):
#     answer = []
#     # Trie로 풀어보자
#     # - 를 포함하여 미리 다 세팅을 해보
#     # resume_trie = {}
#     # 캐시도 사용해보자
#     resume_trie = Trie()
#     language = ['cpp', 'java', 'python', '-']
#     position = ['backend', 'frontend', '-']
#     career = ['junior', 'senior', '-']
#     food = ['chicken', 'pizza', '-']
#     tree_list = [language, position, career, food]
#     for i, t in enumerate(tree_list):
#         resume_trie.tree_setting(i, t, None)
#     for data in info:
#         m = data.split(' ')
#         resume_trie.insert(m)
#     cache = dict()
#     for q in query:
#         q = q.replace('and ', '')
#         convert_s = q.split(' ')
#         if tuple(convert_s) in cache.keys():
#             cnt = cache[tuple(convert_s)]
#         else:
#             cnt = resume_trie.search_count(convert_s)
#             cache[tuple(convert_s)] = cnt
#         answer.append(cnt)
#     print(answer)
#     return answer


# print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
#       "java and backend and junior and pizza 100",  "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]) == [1, 1, 1, 1, 2, 4])
