def solution(left, right):
    answer = 0
    for m in range(left, right+1):
        if convert_num(m) % 2 == 0:
            answer += m
        else:
            answer -= m
    return answer

# 약수의 개수 구하기


def convert_num(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


print(solution(13, 17) == 43)
