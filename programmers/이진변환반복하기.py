from itertools import count


def solution(s: str):
    answer = []
    cycle_cnt = 0
    total_cnt = 0
    while s != '1':
        zero_cnt = s.count('0')
        cycle_cnt += 1
        # 0을 지울수 있으면 remove cnt +=1
        if zero_cnt > 0:
            total_cnt += zero_cnt
            # 0을 제거하기
            s = s.replace('0', '')
        # 0 제거한 문자열 길이 반환
        #print('zero remove :'+s)
        s_len = len(s)
        #print('s len' + str(s_len))
        s = convert_binray(s_len)
        #print('convert binaray :'+s)
    answer = [cycle_cnt, total_cnt]
    return answer


def convert_binray(n):
    s = ''
    while n > 1:
        s = str(n % 2) + s
        n = n // 2
    return '1'+s


print(solution("110010101001") == [3, 8])
print(solution("01110") == [3, 3])
print(solution("1111111") == [4, 1])
