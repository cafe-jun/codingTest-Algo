def solution(N):
    enable_print = N % 10
    answer = ''
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        elif enable_print == 1:
            answer += str(N%10)
        N = N // 10
    return int(answer.strip())
print(solution(54321) == 12345)