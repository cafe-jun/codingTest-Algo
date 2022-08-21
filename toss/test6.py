from collections import defaultdict
import heapq


def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []
    tmp = []
    names_dict = defaultdict(int)
    for i, name in enumerate(names_one):
        names_dict[name] += steps_one[i]

    for i, name in enumerate(names_two):
        names_dict[name] += steps_two[i]

    for i, name in enumerate(names_three):
        names_dict[name] += steps_three[i]

    for v in names_dict.keys():
        heapq.heappush(tmp, (-1*(names_dict[v]), v))

    while tmp:
        answer.append(heapq.heappop(tmp))
    return answer
