from collections import deque


def solution(queue1:list[int], queue2:list[int]):
    answer = -1
    queue1_sum = sum(queue1) 
    queue2_sum = sum(queue2)
    mid = (queue1_sum+queue2_sum)// 2
    move_cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    # 모든 큐를 순회하기위한 길이  
    max_move = len(queue1)*3
    while move_cnt < max_move:
        if queue1_sum == mid and queue2_sum == mid:
            break
        if queue1_sum > mid:
            q_value = q1.popleft()
            queue1_sum -= q_value
            queue2_sum += q_value
            q2.append(q_value)
        elif queue2_sum > mid:
            q_value = q2.popleft()
            queue2_sum -= q_value
            queue1_sum += q_value
            q1.append(q_value)
        move_cnt += 1
    
    if move_cnt >= max_move:
        answer = -1
    else:
        answer = move_cnt        
    return answer
print(solution([4, 6, 5, 1],[4, 6, 5, 1])==0)
print(solution([3, 2, 7, 2],[4, 6, 5, 1])==2)
print(solution([1, 2, 1, 2],[1, 10, 1, 2])==7)
print(solution([1,1],[1,5])==-1)
