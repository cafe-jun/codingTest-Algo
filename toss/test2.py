# 적당히 어려운 문제
# 상위 25% 난이도를 가진 문제중 가장 쉬운 문제

def solution(levels: list[int]):
    answer = 0
    levels.sort()
    one_per_percent = 100 / len(levels)
    percent = 0
    cnt = 0
    for i in range(0, len(levels)+1):
        cnt += 1
        percent += one_per_percent
        if percent > 25:
            cnt -= 1
            break
    if cnt == 0:
        answer = -1
    else:
        answer = levels[-1*(cnt)]
    print(answer)
    return answer


# print(solution([1]) == -1)
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1)

print(solution([1, 2, 4, 4, 5, 6, 7, 8, 9]) == 8)

print(solution([1, 2, 3, 4]) == 4)

print(solution([1, 2, 3, 4]) == 4)
