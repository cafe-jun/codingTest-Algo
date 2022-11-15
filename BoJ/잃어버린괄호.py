
# S = input()


def solution(S: str):
    arr = []
    tmp = ''
    for char in S:
        if ord('0') <= ord(char) <= ord('9'):
            tmp += char
        else:
            if tmp != '':
                arr.append(int(tmp))
                tmp = ''
            arr.append(char)
    total = 0
    switch = '+'
    for n in arr:


print(solution("55-50+40") == -35)
print(solution("10+20+30+40") == 100)
print(solution("00009-00009") == 0)
