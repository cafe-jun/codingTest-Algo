
s = input()


def solution(s: str):
    cnt = 0
    tmp_s = ''
    for c in s:
        if c == ' ':
            if len(tmp_s) > 0:
                tmp_s = ''
                cnt += 1
        else:
            tmp_s += c
    else:
        if len(tmp_s) > 0:
            cnt += 1
    return cnt


print(solution(s))
