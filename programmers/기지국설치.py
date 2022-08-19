from collections import deque


def solution(n, stations, w):
    answer = 0
    current = 1
    stations_q = deque(stations)
    station = stations_q.popleft()
    while current <= n:
        # 현재 위치에서 설치 가능 ?
        # 추후에 확인해보자
        for i in range(1, w+1):
            if current+w+i < station - w:
                pass
                print('기지국 설치')

    print('이분탐색 활용')
    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
