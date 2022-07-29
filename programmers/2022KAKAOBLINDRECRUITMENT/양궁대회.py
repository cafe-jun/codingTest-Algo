# 라이언이 우승할 방법이 있는 경우, return 할 정수 배열의 길이는 11입니다.
# 0 ≤ return할 정수 배열의 원소 ≤ n
# return할 정수 배열의 원소 총합 = n (꼭 n발을 다 쏴야 합니다.)
# return할 정수 배열의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수입니다. ( i는 0~10 사이의 정수입니다.)
# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
# 가장 낮은 점수를 맞힌 개수가 같을 경우 계속해서 그다음으로 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
# 예를 들어, [2,3,1,0,0,0,0,1,3,0,0]과 [2,1,0,2,0,0,0,2,3,0,0]를 비교하면 [2,1,0,2,0,0,0,2,3,0,0]를 return 해야 합니다.
# 다른 예로, [0,0,2,3,4,1,0,0,0,0,0]과 [9,0,0,0,0,0,0,0,1,0,0]를 비교하면[9,0,0,0,0,0,0,0,1,0,0]를 return 해야 합니다.
# 라이언이 우승할 방법이 없는 경우, return 할 정수 배열의 길이는 1입니다.
# 라이언이 어떻게 화살을 쏘든 라이언의 점수가 어피치의 점수보다 낮거나 같으면 [-1]을 return 해야 합니다.

import heapq
from itertools import combinations


def solution(n: int, info: list[int]):
    answer = []
    win_list = []
    m = [i for i in range(11)]
    # 10을 최소로 이기는 경우
    for i in range(1, 11):
        for combin in combinations(m, i):
            result = check_win(info, combin, n)
            if result[1] != [-1]:
                if not win_list:
                    win_list.append(result)
                if (-1)*win_list[0][0] < (-1)*result[0]:
                    win_list.clear()
                    win_list.append(result)
                elif win_list[0][0] == result[0]:
                    win_list.append(result)
    if not win_list:
        return [-1]
    min_answer = win_list[0][1]
    for win_num in win_list:
        target_list = win_num[1]
        for i in range(10, -1, -1):
            if min_answer[i] > target_list[i]:
                break
            elif min_answer[i] < target_list[i]:
                min_answer = target_list
                break
    answer = min_answer
    return answer


def check_win(apeach, target, n):
    arrow = n
    iron = [0]*11
    combi_list = sorted(list(target), reverse=True)
    for score in combi_list:
        apeach_ts = apeach[10-score]
        if arrow < apeach_ts + 1:
            iron[10 - score] += arrow
            break
        iron[10 - score] = apeach_ts + 1
        arrow -= (apeach_ts + 1)
    else:
        iron[10-score] += arrow
    apeach_score = 0
    iron_score = 0
    for i in range(11):
        if apeach[10-i] == 0 and iron[10-i] == 0:
            continue
        if apeach[10-i] < iron[10-i]:
            iron_score += (i)
        else:
            apeach_score += (i)
    else:
        if iron_score > apeach_score:
            return ((-1)*abs(iron_score-apeach_score), iron)
        else:
            return (0, [-1])


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
      == [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1])
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])
      == [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
      )
