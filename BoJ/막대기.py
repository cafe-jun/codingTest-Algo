
n = int(input())


def solution(n: int):
    stick = 64
    cnt = 0
    while stick > 0:
        if n >= stick:
            n -= stick
            cnt += 1
            continue
        stick = stick // 2
    return cnt


print(solution(n))
# print(solution(23))
# print(solution(32))
# print(solution(64))
# print(solution(48))
