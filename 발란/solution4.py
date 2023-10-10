from itertools import combinations

def solution(M, load):
# 모든 물건을 옮길 수 없는 경우 확인
    if max(load) > M:
        return -1

    load.sort(reverse=True)
    trucks = 0
    while load:
        weight = load.pop(0)
        for i in range(len(load)-1, -1, -1):
            if weight + load[i] <= M:
                weight += load.pop(i)
                break
        trucks += 1

    return trucks





print(solution(10,[2,3,7,8])) # result: 2
print(solution(5,[2,2,2,2,2])) # result: 3
print(solution(20,[16,15,9,17,1,3])) # result: 4