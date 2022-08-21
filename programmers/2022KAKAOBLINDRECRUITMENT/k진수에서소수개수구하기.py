

def solution(n, k):
    answer = 0
    n_decimals = convert_n_decimal(n, k)
    n_list = n_decimals.split('0')
    tmp_list = []
    for m in n_list:
        if m.isdecimal():
            tmp_list.append(int(m))
    for num in list(tmp_list):
        if is_prime_route(num) == True:
            answer += 1
    return answer

# n 진법으로 변환


def convert_n_decimal(n, k):
    result = ''
    if k == 10:
        return str(n)
    while n > 0:
        result += str(n % k)
        n = n // k
    return result[::-1]
# 소수 판별 알고리즘


def is_prime_route(x):
    import math
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(solution(1, 3) == 0)
print(solution(437674, 3) == 3)
print(solution(110011, 10) == 2)
