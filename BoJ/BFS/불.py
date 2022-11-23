from collections import deque


f = open('BoJ/test.txt')
# r, c = map(int, f.readline().split())
r, c = map(int, input().split())
matrix = []
temp = []
fire_q = deque()
jin_q = deque()
for i in range(r):
    matrix.append(list(map(str, input().split())))
    # matrix.append(list(map(str, f.readline())))
    if matrix[-1][-1] == '\n':
        matrix[-1].pop()
    for j, point in enumerate(matrix[-1]):
        if point == 'F':
            fire_q.append((i, j))
        elif point == 'J':
            jin_q.append((i, j, 0))
            temp.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    jx, jy, move = jin_q.popleft()
    if 0 <= njx < r and 0 <= njy < c:
        if matrix[jx][jy] == 'F':
            continue
    for i in range(4):
        njx, njy = dx[i]+jx, dy[i]+jy
        if 0 <= njx < r and 0 <= njy < c:
            if matrix[njx][njy] == '.' and (njx, njy) not in temp:
                jin_q.append((njx, njy, move+1))
                matrix[njx][njy] = 'J'
    else:
        if len(jin_q) == 0:
            print(move+1)
            break
    fx, fy = fire_q.popleft()
    for i in range(4):
        nfx, nfy = dx[i]+fx, dy[i]+fy
        if 0 <= nfx < r and 0 <= nfy < c:
            if matrix[nfx][nfy] in ['.', 'J']:
                fire_q.append((nfx, nfy))
                matrix[nfx][nfy] = 'F'
