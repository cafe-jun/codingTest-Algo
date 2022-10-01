def solution(n):
    return int(convert(n), 3)


def convert(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    return rev_base


print(solution(45) == 7)
print(solution(125) == 229)
