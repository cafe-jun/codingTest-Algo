from collections import Counter
import re

def solution(id_list, report:list[str], k):
    answer = []
    # counter = Counter(report)
    # print(counter)
    # 뮤지가 누구를 신고했나 ? 
    # 신고를 당한 사람이 Key , 신고를 하는사람 Value 
    # { frodo : ["",""]  }
    # dictionary 구조가 두개 필요하겠네? 
    #  value array 를 3개 가지고있는사람이면 
    # {count 하기 } count 
    r_dict = dict()
    
    for r in report:
        reported,user_id = r.split(' ')
        if user_id not in r_dict.keys():
            r_dict[user_id] = [reported]
        else:
            if reported not in r_dict[user_id]:
                v = r_dict.get(user_id)
                v.append(reported)
                r_dict[user_id] = v
    
    u_dict = dict()
    for id in id_list:
        u_dict[id] =0

    for r_key in r_dict.keys():
        if len(r_dict[r_key]) >= k:
            for id in r_dict[r_key]:
                u_dict[id] +=1
    
    for v in u_dict.values():
        answer.append(v)
    return answer



print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))