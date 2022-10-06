from collections import Counter


def solution(str1 : str, str2: str):
    answer = 0
    str1_set = [] 
    str2_set = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_set.append(str1[i:i+2].upper())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_set.append(str2[i:i+2].upper())
    str1_c = Counter(str1_set)
    str2_c = Counter(str2_set)
    total_set = set()
    for s in list((str1_c.keys())):
        total_set.add(s)
    for s in list((str2_c.keys())):
        total_set.add(s)
    total_cnt = 0
    equal_cnt = 0
    for t in list(total_set):
        if t in list(str1_c.keys()) and t in list(str2_c.keys()):
            equal_cnt += min(str1_c[t],str2_c[t])
            total_cnt += max(str1_c[t],str2_c[t])
        else:
            if t in list(str1_c.keys()):
                total_cnt += str1_c[t]
            else:
                total_cnt += str2_c[t]
              
    if total_cnt > 0:
        answer = int((equal_cnt/total_cnt)*65536)
    else:
        answer = 65536
    return answer


print(solution("FRANCE","french") == 16384)
print(solution("handshake","shake hands") == 65536)
print(solution("aa1+aa2","AAAA12") == 43690)
print(solution("E=M*C^2","e=m*c^2") == 65536)



# 가독성이 좋은 잘된 코드 
# def solution(str1, str2):

#     list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
#     list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

#     tlist = set(list1) | set(list2)
#     res1 = [] #합집합
#     res2 = [] #교집합

#     if tlist:
#         for i in tlist:
#             res1.extend([i]*max(list1.count(i), list2.count(i)))
#             res2.extend([i]*min(list1.count(i), list2.count(i)))

#         answer = int(len(res2)/len(res1)*65536)
#         return answer

#     else:
#         return 65536