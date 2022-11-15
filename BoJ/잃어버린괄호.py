
S = input()


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
    else:
        arr.append(int(tmp))

    total_num = 0
    split_num = 0
    switch = False
    for n in arr:
        if switch == True:
            if n == '-':
                total_num += -1*split_num
                split_num = 0
            elif n == '+':
                continue
            else:
                split_num += n
        else:
            if n == '-':
                switch = True
            elif n == '+':
                continue
            else:
                total_num += n
    else:
        if switch == True:
            total_num += -1*split_num
    return total_num


print(solution(S))

# print(solution("55-50+40") == -35)
# print(solution("10+20+30+40") == 100)
# print(solution("00009-00009") == 0)
