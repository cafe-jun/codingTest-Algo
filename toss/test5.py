from collections import defaultdict


def solution(tasks):
    answer = 0
    task_dict = defaultdict(int)
    for tasks in tasks:
        task_dict[tasks] += 1

    for k in task_dict.keys():
        if task_dict[k] <= 1:
            answer = -1
            break
        answer += task_dict[k] // 3
        task_dict[k] = task_dict[k] % 3
        answer += task_dict[k] // 2
        task_dict[k] = task_dict[k] % 2
        if task_dict[k] >= 1:
            answer += 1

    return answer


# print(solution([1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2]))
# print(solution([4, 1, 1, 1, 1, 2, 3]))
print(solution([1, 1, 2, 2]))
