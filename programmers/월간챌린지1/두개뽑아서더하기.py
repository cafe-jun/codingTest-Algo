from itertools import combinations


def solution(numbers):
    answer = set()
    for nums in combinations(numbers, 2):
        answer.add(sum(nums))
    return sorted(list(answer))


print(solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7])
print(solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12])
