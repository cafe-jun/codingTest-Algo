
import heapq


def solution(n: int, t: int, m: int, timetable: list[str]):
    answer = ''
    tmp_list = []
    for time in timetable:
        dt = time
        dm = dt.split(':')
        total_m = int(dm[0])*60+int(dm[1])
        heapq.heappush(tmp_list, total_m)
    start_minute = 540
    end_minute = 0
    chart = dict()
    for i in range(1, n+1):
        chart[start_minute] = list()
        while True:
            if not tmp_list:
                break
            if len(chart[start_minute]) < m:
                if start_minute >= tmp_list[0]:
                    chart[start_minute].append(heapq.heappop(tmp_list))
                else:
                    break
            else:
                break
        start_minute += t
    else:
        end_minute = start_minute-t
    # 양끝과 중간일때 다름
    # 중간일때는 중간에 탈수가 있으면
    tmp_time = 0
    if len(chart[end_minute]) < m:
        tmp_time = end_minute
    else:
        tmp_time = chart[end_minute][-1]-1

    hour, minute = divmod(tmp_time, 60)
    answer += str(hour).rjust(2, '0') + ':'
    answer += str(minute).rjust(2, '0')
    return answer


print(solution(10, 25, 1, ["09:00", "09:10", "09:20", "09:30", "09:40", "09:50",
                           "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]) == "10:29")
print(solution(10, 1, 5, ["09:00", "09:00",
      "09:00", "09:00", "09:00"]) == "09:09")
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]) == "09:00")
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]) == "09:09")
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]) == "08:59")
print(solution(1, 1, 5, ["00:01", "00:01",
      "00:01", "00:01", "00:01"]) == "00:00")
print(solution(1, 1, 1, ["23:59"]) == "09:00")
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
      "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]) == "18:00")
