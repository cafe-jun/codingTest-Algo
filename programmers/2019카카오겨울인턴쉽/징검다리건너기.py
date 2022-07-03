from collections import deque
import heapq


def solution(stones: list[int], k: int):
    answer = 0
    x = 1
    # 다 건넌 징검다리를 저장
    end_stone = []
    # 이진탐색 코드
    start = 1
    end = max(stones)
    while start <= end:
        mid = (start+end) // 2
        # 4 번을 할수 있는지 확인
        zero_cnt = 0
        for i, s in enumerate(stones):
            if stones[i] < mid:
                zero_cnt += 1
            else:
                zero_cnt = 0
            if zero_cnt == k:
                end = mid - 1
                break
        else:
            start = mid+1
            answer = mid
    return answer


def check(end_stone: list, k):
    # 연속된 k개의 숫자 찾기
    # heaq 를 이용하여 풀기
    is_check = False
    q = deque()
    for i in range(len(end_stone)):
        q.append(heapq.heappop(end_stone))
        if len(q) == k:
            # 연속된 수
            if q[-1] - q[0] == k-1:
                is_check = False
                break
            else:
                q.popleft()
    else:
        is_check = True
    return is_check


# print(solution([2, 1, 1, 1, 1, 1, 1, 1, 1, 200000000], 5))

# print(solution([2, 200000000], 5))

# print(solution([2, 2, 2, 2, 1, 1, 1, 1], 3))

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3)


# while stone_list:
#         x = stone_list[0][0]
#         while stone_list:
#             # 띄어 다닐수있을까 ?
#             # 현재 포인트로 부터 연속된 k 개의수가 있으면 못건넘
#             if stone_list[0][0] > x:
#                 break
#             else:
#                 v, n = heapq.heappop(stone_list)
#                 # 못건너는 스톤이 몇개야 ?
#                 heapq.heappush(end_stone, n)
#                 if check(end_stone.copy(), k) == False:
#                     is_check = False
#                     answer = v
#                     break
#         if is_check == False:
#             break
#     if is_check == True:
#         answer = x
