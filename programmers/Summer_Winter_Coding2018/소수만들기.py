from itertools import combinations
import math


def solution(nums):
    answer = 0
    for combi in combinations(nums, 3):
        combi_num = sum(list(combi))
        if is_prime_route(combi_num) == True:
            answer += 1

    return answer


def is_prime_route(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(solution([1, 2, 3, 4]) == 1)

print(solution([1, 2, 7, 6, 4]) == 4)
