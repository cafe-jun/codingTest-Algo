import itertools


def solution(n):
    answer = []
    t = [[0 for j in range(i+1)] for i in range(n)]
    x, y = [0, 0]
    point = 1
    i, j = (0, 0)
    direction = 'down'
    while n > 0:
        for _ in range(n):
            t[x+i][y+j] = point
            point += 1
            if direction == 'down':
                x += 1
            elif direction == 'left':
                y += 1
            elif direction == 'up':
                x -= 1
                y -= 1
        n -= 1
        if direction == 'down':
            direction = 'left'
            x -= 1
            y += 1
        elif direction == 'left':
            direction = 'up'
            x -= 1
            y -= 2
        elif direction == 'up':
            direction = 'down'
            x += 2
            y += 1
    # for m in t:
    #     for num in m:
    #         answer.append(num)
    answer = list(itertools.chain(*t))

    return answer


print(solution(4))
print(solution(5))
print(solution(6))
