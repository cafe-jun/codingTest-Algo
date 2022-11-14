from copy import copy
import heapq


def solution(a: list[int]):
    if len(a) == 1:
        return 1
    if len(a) == 2:
        return 2
    answer = 2
    idx = 1
    # min 말고 heapq 를 사용해보자 
    right_list = []
    left_min = a[0]
    for k,num in enumerate(a[idx+1:]):
        heapq.heappush(right_list,(num,k+1))
    right_min = right_list[0][0]
    # print(a[idx:len(a)-1])

    for i,target in enumerate(a[idx:len(a)-1]):
        if target == right_min:
            # 1부터 시작하기 때문에 
            heapq.heappop(right_list)
            # 후보군 줄이기 
            while (i+1) > right_list[0][1]:
                heapq.heappop(right_list)
            right_min = right_list[0][0]
        if not (right_min < target and left_min < target):
            answer += 1
        left_min = min(left_min,target)
    # 사용 가능한 비교 => 큰,t,큰 | 큰,t,작 | 작,t,큰
        # print('currnet_idx :' + str(a[idx]))
        # print('left_min :' + str(left_min))
        # print('right_min :' + str(right_min))
        # min 이 아니라 heaq 을 사용해보자 
        # if (left_min < a[idx] < right_min)or (right_min < a[idx] < left_min) or (a[idx] < right_min and a[idx] < left_min):
        #     answer += 1
        # heapq.heappush(left_min,a[idx])
        # heapq.heappush(right_min,a)
        
        # idx +=1
        
        # if right_min_idx == idx:
        #     if idx+1 < a_len: 
        #         right_min = min(a[idx+1:])
        #         right_min_idx = a.index(right_min)
        #     else:
        #         right_min = a[-1]
        #         right_min_idx = idx+1
        # else:
        #     right_min = min(right_min,a[idx])
    return answer

# print(solution([9,-1,-5]))
# print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
print(solution([-16,27,-80,-65,-2,58,-92,-71,-68,-61,-33]))




# def solution(a):
#     answer = 2
#     idx = 1
#     a_len = len(a)
#     left_min = a[0]
#     right_min = min(a[idx+1:])
#     right_min_idx = a.index(right_min)
#     # 사용 가능한 비교 => 큰,t,큰 | 큰,t,작 | 작,t,큰
#     while idx < a_len-1:
#         # print('currnet_idx :' + str(a[idx]))
#         # print('left_min :' + str(left_min))
#         # print('right_min :' + str(right_min))
#         if (left_min < a[idx] < right_min)or (right_min < a[idx] < left_min) or (a[idx] < right_min and a[idx] < left_min):
#             answer += 1
#         left_min = min(left_min,a[idx])
#         idx +=1
#         if right_min_idx == idx:
#             if idx+1 < a_len: 
#                 right_min = min(a[idx+1:])
#                 right_min_idx = a.index(right_min)
#             else:
#                 right_min = a[-1]
#                 right_min_idx = idx+1
#         else:
#             right_min = min(right_min,a[idx])
#     return answer