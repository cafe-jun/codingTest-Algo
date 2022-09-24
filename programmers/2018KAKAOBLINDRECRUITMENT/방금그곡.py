# 음의 사용 :  C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# #이 들어간 음을 잘 처리를 해줘야한다
# 중간 부터
# 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다
from datetime import datetime
import heapq


def solution(m, musicinfos):
    answer = ''
    tmp_answer = []
    for idx, musicinfo in enumerate(musicinfos):
        info = musicinfo.split(',')
        start_time = info[0]
        end_time = info[1]
        score = info[3]
        name = info[2]
        start_d = datetime.strptime(start_time, "%H:%M")
        end_d = datetime.strptime(end_time, "%H:%M")
        minute = int(abs(start_d.timestamp()-end_d.timestamp())//60)
        # 목
        p, v = divmod(len(m), len(score))
        music = score*(p+1)
        if v > 0:
            music += score

        # 나머지가 있다면
        # 중간 부터 들을 경우도 생각을 해야한다
        # 음악 재생시간 < 음악 악보 길이인 경우, 음악의 처음부터 ~ 음악 재생 길이([0~음악 재생 길이] ) 까지만 본다.
        for i in range(len(music)-len(m)):
            # print(music[i:i+len(m)])
            if music[i:i+len(m)] == m:
                #  다음 내용 #체크
                if music[i+len(m):i+len(m)+1] != '#' and i+len(m)+1 < len(music):
                    heapq.heappush(tmp_answer, (-minute, idx, name))
                    break

    if not tmp_answer:
        answer = '(None)'
    else:
        answer = heapq.heappop(tmp_answer)[2]
    return answer


print(solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"]) == "(None)")
print(solution("A#AB#", ["13:00,13:03,HAPPY,B#A#A"]) == "HAPPY")
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB",
      "13:00,13:05,WORLD,ABCDEF"]) == "HELLO")
print(solution("CC#BCC#BCC#BCC#B", [
      "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]) == "FOO")
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB",
      "13:00,13:05,WORLD,ABCDEF"]) == "WORLD")
print('test')
