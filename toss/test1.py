import heapq


def solution(s):
    answer = 0
    tmp = []
    heapq.heappush
    for i in range(len(s)-2):
        substring = s[i:i+3]
        if substring[0] == substring[1] and substring[0] == substring[2] and substring[2] == substring[1]:
            heapq.heappush(tmp, (-1*int(substring[0]), substring))
    else:
        if tmp:
            _, sub = heapq.heappop(tmp)
            answer = str(sub)
        else:
            answer = - 1
    return answer


print(solution('111999333'))
