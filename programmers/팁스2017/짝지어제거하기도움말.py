class Stack:
    size: int

    def __init__(self, max_size):
        self.size = max_size


def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return 0 if len(stack) > 0 else 1


print(solution("baabaa") == 1)
print(solution("cdcd") == 0)
