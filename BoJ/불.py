
# input().split()
from collections import deque
from copy import copy

answer = 1e9
f = open('BoJ/test.txt')
r, c = map(int, f.readline().split())
# r, c = map(int, input().split())
matrix = [['O' for _ in range(r+2)] for _ in range(c+2)]
start = None
fires = deque()
for i in range(r):
    string = f.readline()
    # string = input()
    for j, s in enumerate(string):
        if s != '\n':
            if s == 'J':
                start = (i+1, j+1, 0)
            if s == 'F':
                fires.append((i+1, j+1))
            matrix[i+1][j+1] = s
f.close()
print('')
q = deque()
q.append(start)
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
visited = []
visited.append((start[0], start[1]))
turn_cost = 0
# while q:
#     y, x, cost = q.popleft()
#     if matrix[y][x] == 'O':
#         answer = min(cost, answer)
#         continue
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny <= c+1 and 0 <= nx <= r+1:
#             if (matrix[ny][nx] == '.' or matrix[ny][nx] == 'O') and (ny, nx) not in visited:
#                 q.append((ny, nx, cost+1))
#                 visited.append((ny, nx))
#     if turn_cost == cost:
#         tmp_fires = deque()
#         while fires:
#             a, b = fires.popleft()
#             for i in range(4):
#                 na = a + dy[i]
#                 nb = b + dx[x]
#                 if 0 <= na <= c+1 and 0 <= nb <= r+1:
#                     if matrix[na][nb] == '.':
#                         matrix[na][nb] = 'F'
#                         tmp_fires.append((na, nb))
#         fires = copy(tmp_fires)


if answer == 1e9:
    print('IMPOSSIBLE')
else:
    print(answer)
