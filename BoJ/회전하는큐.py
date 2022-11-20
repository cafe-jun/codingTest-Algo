# 문제 이해 불가 
# https://www.acmicpc.net/problem/1021

# 
from collections import deque

N,M = map(int,input().split())
# 뽑아 내려고 하는수 mq 
mq = list(map(int,input().split()))


def solution(n: int,m: list[int]):
    # 1 부터 n 까지의 deque 생성하기 
    answer = 0
    q = deque([i+1 for i in range(n)])
    #  뽑아내려고 하는 수를 담은 dequeue
    mq = deque(m)
    while mq:
        # 뽑아내려고 하는수 
        num = mq.popleft()
        # 뽑아내려고 하는수의 위치 
        num_idx = q.index(num)
        # 앞에서 가까운지 뒤에서 가까운지 판단하여 방향 설정 
        direction = 'left' if num_idx - 0 <= len(q) - num_idx else 'right'
        # 회전 함수 
        def cycle_queue(direction: str):
            cnt = 0
            if 'left' == direction:
                while q[0] != num:
                    # 앞에서 뺀걸 뒤로 넣기 
                    q.append(q.popleft())
                    # 회전 하는 카운팅 
                    cnt += 1
            else:
                while q[0] != num:
                    # 뒤에서 뺸걸 앞에서 넣기 
                    q.appendleft(q.pop())
                    # 회전 하는 카운팅 
                    cnt += 1
            # 1 번 조건 실행 
            q.popleft()       
            return cnt
        # 회전 숫자 추가 
        answer += cycle_queue(direction)
    return answer
        
        

print(solution(N,mq))



# print(solution(10,[1,2,3]) == 0)
# print(solution(10,[2,9,5]) == 8)
# print(solution(32,[27,16,30,11,6,23]) == 59)
# print(solution(10,[1,6,3,2,7,9,8,4,10,5]) == 14)



# def solution(n: int,m: list[int]):
#     q = deque() 
#     for i in range(n):
#         q.append(i+1)
#     mq = deque(m)
#     two_cnt = 0
#     three_cnt = 0
#     while mq:
#         num = mq.popleft()
#         # 앞에서 가까운지 뒤에서 가까운지 판단 
#         num_idx = q.index(num)
#         left_len = num_idx - 0
#         right_len = len(q) - num_idx
#         if left_len <= right_len:
#             while True:
#                 if q[0] == num: 
#                     q.popleft()
#                     break;
#                 else:
#                     q.append(q.popleft())
#                     two_cnt += 1
#         else:
#             while True:
#                 if q[0] == num: 
#                     q.popleft()
#                     break;
#                 else:
#                     q.appendleft(q.pop())
#                     three_cnt += 1
#     return two_cnt + three_cnt