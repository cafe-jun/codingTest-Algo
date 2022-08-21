from itertools import permutations


def solution(k, dungeons):
    answer = -1
    v_list = list(range(len(dungeons)))
    # 사용 체력이 적은 상태
    max_result = 0
    for value in permutations(v_list, len(v_list)):
        current_k = k
        cnt = 0
        for i in list(value):
            require, consumer = dungeons[i]
            if current_k >= require:
                current_k -= consumer
                cnt += 1
        max_result = max(max_result, cnt)
    answer = max_result
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
