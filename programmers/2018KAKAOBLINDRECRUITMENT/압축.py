from collections import deque

# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.


def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            print(msg[:tt], msg.__len__())
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer

# def solution(msg):
#     answer = []
#     keyword = dict()
#     for i in range(26):
#         keyword[chr(i+65)] = i+1
#     max_cnt = 27
#     w = ''
#     key_q = deque(list(msg))
#     dp = []
#     c = ''
#     while key_q:
#         # 현재 입력 w
#         # 다음 글자 c
#         w += key_q.popleft()
#         if len(key_q) > 0:
#             c = key_q[0]
#         else:
#             c = ''

#         if w+c not in dp:
#             if w in keyword.keys():
#                 answer.append(keyword[w])
#                 keyword[w+c] = max_cnt
#                 dp.append(w+c)
#                 max_cnt += 1
#                 w = ''
#             else:
#                 answer.append(keyword[w])
#     if w != '':
#         answer.append(keyword[w])
#     return answer


print(solution("KAKAO") == [11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT") == [
      20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB") == [1, 2, 27, 29, 28, 31, 30])
