dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(grid):
    global visited, n, m
    n = len(grid)
    m = len(grid[0])
    answer = []
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    for sx in range(n):
        for sy in range(m):
            for d in range(4):
                if not visited[sx][sy][d]:
                    rst = simul(sx, sy, d, grid)
                    if rst != 0:
                        answer.append(rst)
    answer.sort()
    return answer


def simul(sx, sy, sd, grid):
    global visited
    x, y, d = sx, sy, sd
    cnt = 0
    visited[sx][sy][sd] = True
    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1

        if grid[x][y] == 'R':
            d = (d+1) % 4
        elif grid[x][y] == 'L':
            d = (d-1) % 4
        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))


# def solution(grid: list[str]):
#     answer = []
#     matrix = [[c for c in i] for i in grid]
#     light = []
#     visited = []
#     direction = {'DOWN': [1, 0], 'UP': [-1, 0],
#                  'LEFT': [0, 1], 'RIGHT': [0, -1]}

#     # 빛이 어디서 어디 방향으로 쏘는지에대한 값이있어야한다
#     light.append((0, 0, 'DOWN'))
#     visited.append((0, 0, 'DOWN'))
#     cnt = 0
#     x_len = len(grid)
#     y_len = len(grid[0])
#     init_grid = matrix[0][0]
#     while True:
#         x, y, d = light.pop()
#         if x < 0:
#             x = x_len - 1
#         elif x >= x_len:
#             x = 0
#         if y < 0:
#             y = y_len - 1
#         elif y >= y_len:
#             y = 0

#         g = matrix[x][y]
#         print('x :', x, ' y:', y, ' direction:', d, 'current', g, 'cnt: ', cnt)
#         if g == 'L':
#             if d == 'DOWN':
#                 d = 'LEFT'
#             elif d == 'UP':
#                 d = 'RIGHT'
#             elif d == 'LEFT':
#                 d = 'UP'
#             elif d == 'RIGHT':
#                 d = 'DOWN'
#         elif g == 'R':
#             if d == 'DOWN':
#                 d = 'RIGHT'
#             elif d == 'UP':
#                 d = 'LEFT'
#             elif d == 'LEFT':
#                 d = 'DOWN'
#             elif d == 'RIGHT':
#                 d = 'UP'
#         l = direction[d]

#         x += l[0]
#         y += l[1]
#         cnt += 1
#         light.append((x, y, d))
#     return answer
