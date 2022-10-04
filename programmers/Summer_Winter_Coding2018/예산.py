def solution(d, budget):
    answer = 0
    sort_d = sorted(d)
    for s in sort_d:
        if s <= budget:
            answer += 1
            budget -= s
        else:
            break
    return answer


print(solution([1, 3, 2, 5, 4], 9) == 3)
print(solution([2, 2, 3, 3], 10) == 4)
