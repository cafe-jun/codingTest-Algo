from datetime import datetime, timedelta


def solution(lines: list[str]):
    answer = 0
    stl = []
    # 우선순위 큐
    # 시간 더하기 가장 빠른 시간을 앞으로
    for line in lines:
        dtt = line.split(' ')
        dm = dtt[0]+' '+dtt[1]
        dt = datetime.strptime(dm, "%Y-%m-%d %H:%M:%S.%f")
        dt_mil = float(dtt[2][:-1])*1000
        start_timestamp = dt-timedelta(milliseconds=dt_mil)
        start_timestamp = (start_timestamp.timestamp()*1000)+1
        end_timestamp = dt.timestamp()*1000
        stl.append((start_timestamp, end_timestamp))
    # 요청 처음과 끝이 트래픽이 달라짐
    max_cnt = 0
    for s in stl:
        s_max_cnt = 0
        e_max_cnt = 0
        start, end = s
        for t in stl:
            # 요청 처음부터 +1 초
            t_start, t_end = t
            if start <= t_start <= start+999 or t_start <= start+999 <= t_end:
                s_max_cnt += 1

            # 요청 끝에 1초
            if end <= t_end <= end+999 or t_start <= end+999 <= t_end:
                e_max_cnt += 1
        print(s_max_cnt, e_max_cnt)
        max_cnt = max(max_cnt, max(s_max_cnt, e_max_cnt))
    # print(max_cnt)
    answer = max_cnt
    return answer


# print(solution([
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]) == 1)
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
