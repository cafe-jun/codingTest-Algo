def power_modulo(A, B, C):
    result = 1
    A = A % C  # A를 C로 나눈 나머지로 초기화

    while B > 0:
        if B % 2 == 1:  # B가 홀수인 경우
            result = (result * A) % C

        A = (A * A) % C
        B //= 2

    return result

A, B, C = map(int, input().split())
print(power_modulo(A, B, C))