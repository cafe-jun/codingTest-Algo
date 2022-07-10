def solution(s):
    answer = ''
    tmp = ''
    d = dict()

    for c in s:
        if c.isdigit():
            if tmp != '':
                answer += tmp
            answer += str(c)
            tmp = ''
        else:
            tmp += c
    return int(answer)
