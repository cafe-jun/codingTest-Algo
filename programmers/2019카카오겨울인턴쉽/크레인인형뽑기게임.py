from shutil import move


def solution(board: list[int], moves: list[int]):
    answer = 0
    b_len = len(board)
    stack = [[] for _ in range(b_len+1)]
    for b in reversed(board):
        for i in range(len(b)):
            if b[i] != 0:
                stack[i+1].append(b[i])

        print(b)
    bucket = []
    for n in moves:
        if len(stack[n]) <= 0:
            continue
        if len(bucket) > 0:
            if bucket[-1] == stack[n][-1]:
                answer += 2
                bucket.pop()
                stack[n].pop()
            else:
                bucket.append(stack[n].pop())
        else:
            bucket.append(stack[n].pop())

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
      0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]) == 4)
