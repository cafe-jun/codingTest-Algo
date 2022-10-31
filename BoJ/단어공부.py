from collections import defaultdict

s = input()


def solution(s: str):
    d = defaultdict(int)
    for c in s:
        d[c.upper()] += 1
    max_num = 0
    ch_arr = []
    for key in d.keys():
        if d[key] > max_num:
            ch_arr.clear()
            ch_arr.append(key)
            max_num = d[key]
        elif d[key] == max_num:
            ch_arr.append(key)
    return '?' if len(ch_arr) > 1 else ch_arr[0]


print(solution(s))
