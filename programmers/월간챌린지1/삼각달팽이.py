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
    answer = list(itertools.chain(*t))
    return answer


print(solution(4) == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
print(solution(5) == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
print(solution(6) == [1, 2, 15, 3, 16, 14, 4, 17,
      21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])
