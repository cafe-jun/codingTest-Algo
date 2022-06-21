

from collections import Counter
from copy import copy

def solution (a):
    elements = Counter(a)
    answer = -1
    for k in elements.keys():
        if elements[k] <= answer:
            continue
        common_cnt = 0
        idx = 0
        while idx < len(a)-1:
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx +=1 
                continue
            common_cnt +=1
            idx += 2
            
        answer = max(common_cnt,answer)
    if answer == -1:
        return 0
    else:
        return answer * 2

# def solution(a: list[int]):
#     answer = -1
    
#     # Count 라는 함수를 이용하여 개수를 가져오자 
#     # 부분 수열의 교집합을 만들어야하기 때문에 각 원소 별로 가져온다 
#     # 작업 Queue 도 가져 온다 
#     # 처음에 넣고 시작하자 
#     # hint : 슈퍼수열 만들기 
    
#     idx_dict = dict()
#     for i,n in enumerate(a):
#         if n not in idx_dict.keys():
#             idx_dict[n] = [i]
#         else:
#             idx_dict[n].append(i)
            
#     result = []
#     for k in idx_dict.keys():
#         cnt = len(idx_dict[k])
#         array = idx_dict[k]
#         idx = -1
#         # a 의 길이 
#         while idx < len(array)-1:
#             idx +=1
#             if len(array) >1:
#                 if idx == 0:
#                     if array[idx+1] == 1:
#                         cnt -= 1
#                     else:
#                         continue
                
#                 if idx == len(array)-1:
#                     if array[idx] - array[idx-1] <=1:
#                         cnt -=1
#                     else:
#                         continue
   
#                 if array[idx+1]-array[idx-1] <=1:
#                     cnt -=1
#             else:
#                 cnt -=1
            
#         result.append(cnt*2)
#         answer = max(result)
#         return answer

     
    

print(solution([0]) == 0)
print(solution([5,2,3,3,5,3]) == 4)
print(solution([0,3,3,0,7,2,0,2,2,0]) == 8)
