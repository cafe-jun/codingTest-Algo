
from itertools import permutations
from collections import deque
from copy import copy


def solution(user_id: list[str], banned_id: list[str]):
    answer = 0
    temp = []
    for l in permutations(user_id, len(banned_id)):
        l_list = list(l)
        for i in range(len(banned_id)):
            if id_mapping(l_list[i], banned_id[i]) == False:
                break
        else:
            l_list.sort()
            temp.append(l_list)

    answer_list = list(set(map(tuple, temp)))
    answer = len(answer_list)
    return answer


def id_mapping(user_id, banner_id):
    is_check = False
    if len(banner_id) == len(user_id):
        for i in range(len(banner_id)):
            if banner_id[i] != '*' and user_id[i] != banner_id[i]:
                break
        else:
            is_check = True
    return is_check


print(solution(["frodo", "fradi", "crodo",
      "abc123", "frodoc"], ["fr*d*", "abc1**"]) == 2)

print(solution(["frodo", "fradi", "crodo", "abc123",
      "frodoc"], ["*rodo", "*rodo", "******"]) == 2)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]) == 3)

# def solution(user_id: list[str], banned_id: list[str]):
#     global temp
#     answer = 0
#     temp = []
#     for banner in banned_id:
#         temp.append([])
#         for user in user_id:
#             if id_mapping(user, banner) == True:
#                 temp[-1].append(user)
#     # 한개를 뽑을때마다 그 다음거에는 전에 있는 Id 가 나와서는 안된다  다른 리스트를 뽑아야한다
#     # 2 1 2
#     l = []
#     l.append([])
#     for t in list(temp.pop(0)):
#         l[-1].append([t])
#     idx = 0

#     while len(temp) - 1 > idx:

#         for t in temp[idx]:
#             print(t)
#             l.append([])
#             for i in l[len(l)-2]:
#                 if t not in i:
#                     k = copy(i)
#                     k.append(t)
#                 l[-1].append(k)
#         idx += 1
#     return answer
# 순서 상관없이
