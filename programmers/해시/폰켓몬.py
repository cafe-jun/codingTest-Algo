from collections import defaultdict


def solution(nums):
    answer = 0
    num_dict = defaultdict(int)
    len_num = len(nums) // 2
    for num in nums:
        num_dict[num] += 1
    len_dict = len(num_dict.keys())
    if len_dict < len_num:
        answer = len_dict
    else:
        answer = len_num
    return answer


print(solution([3, 1, 2, 3]) == 2)
print(solution([3, 3, 3, 2, 2, 4]) == 3)
print(solution([3, 3, 3, 2, 2, 2]) == 2)
