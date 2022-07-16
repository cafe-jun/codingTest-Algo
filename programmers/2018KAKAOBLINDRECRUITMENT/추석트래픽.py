from collections import deque
from datetime import datetime, timedelta
import heapq
import time


def solution(lines: list[str]):
    answer = 0
    stl = []
    # 우선순위 큐
    # 시간 더하기 가장 빠른 시간을 앞으로
    for line in lines:
        date1 = line
        dtt = date1.split(' ')
        dm = dtt[0]+' '+dtt[1]
        dt = datetime.strptime(dm, "%Y-%m-%d %H:%M:%S.%f")
        dt_mil = float(dtt[2][:-1])*1000
        start_timestamp = dt-timedelta(milliseconds=dt_mil)
        end_timestamp = dt
        heapq.heappush(stl, (start_timestamp.timestamp() *
                       1000+1, end_timestamp.timestamp()*1000))
    max_cnt = 0

    return answer


print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]) == 1)
print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]) == 2)
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]) == 7)
