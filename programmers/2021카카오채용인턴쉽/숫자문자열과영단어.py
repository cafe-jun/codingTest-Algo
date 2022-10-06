def solution(s):
    answer = ''
    tmp = ''
    d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for c in s:
        if c.isdigit():
            answer += str(c)
        else:
            tmp += c
        if tmp in d.keys():
            answer += str(d[tmp])
            tmp = ''
    return int(answer)


print(solution("one4seveneight") == 1478)
print(solution("23four5six7") == 234567)
print(solution("2three45sixseven") == 234567)
print(solution("123") == 123)
