# 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
# 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
# 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
# orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
from collections import defaultdict
import heapq
from itertools import combinations

def solution(orders: list[str], course:list[int]):
    answer = []
    # 문자열이 총 몇개인지 확인 
    s_course = set()
    for c in course:
        for o in orders:
            for com in combinations(set(o),c):
                sort_list = sorted(com)
                s_course.add(tuple(sort_list))
        
    s_list = list(s_course)
    menu = defaultdict(int)
    for combin in s_list:
        for order in orders:
            if course_check(order,combin) == True:
                sorted_combin = ''.join(combin)
                menu[sorted_combin] += 1
    len_menu = defaultdict(list)
    max_count = defaultdict(int)
    for k in menu.keys():
        if menu[k] > 1:
            if max_count[len(k)] < menu[k]:
                max_count[len(k)] = menu[k]
                len_menu[len(k)].clear()
                len_menu[len(k)].append(k)
            elif max_count[len(k)] == menu[k]:
                len_menu[len(k)].append(k)
            
    tmp_list = []
    for v in len_menu.values():
        for j in v:
            heapq.heappush(tmp_list,j)
    while tmp_list:
        answer.append(heapq.heappop(tmp_list))
    return answer


def course_check(order,combin):
    is_check = False;
    for c in combin:
        if c not in list(order):
            break
    else:
        is_check = True
    return is_check

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])==["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"],[2,3,4])==["WX", "XY"])


    # 최소 매뉴 2개 이상 
    # max_num = 1
    # max_list = []
    # for idx,m in enumerate(course_list):
    #     max_list.append([])
    #     for k in m:
    #         if max_num < k[1]:
    #             max_num = k[1]
    #             max_list[idx].clear()
    #             max_list[idx].append(k[0])
    #         elif max_num == k[1] and k[1] > 1:
    #             max_list[idx].append(k[0])
    #     else:
    #         max_num = 1