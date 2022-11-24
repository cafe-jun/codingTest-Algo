from collections import deque


f = open('BoJ/test.txt')
r, c = map(int, f.readline().split())
# r, c = map(int, input().split())
matrix = [['.' for _ in range(c+2)] for _ in range(r+2)]
temp = []
fire_q = deque()
jin_q = deque()
# 외벽을 쌓아 보자 
for i in range(r):
    arr = list(map(str, f.readline().strip()))
    # arr = list(map(str, input().strip()))
    for j,a in enumerate(arr):
        matrix[i+1][j+1] = a
        if a == 'F':
            fire_q.append((i+1,j+1))
        elif a == 'J':
            jin_q.append((i+1,j+1,0))
            temp.append((i+1,j+1))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
while True:
    if len(fire_q) > 0:
        fx, fy = fire_q.popleft()
        for i in range(4):
            nfx, nfy = dx[i]+fx, dy[i]+fy
            if 0 < nfx <= r and 0 < nfy <= c:
                if matrix[nfx][nfy] in ['.', 'J']:
                    fire_q.append((nfx, nfy))
                    matrix[nfx][nfy] = 'F'
    
    if len(jin_q) > 0:
        jx, jy, move = jin_q.popleft()
        if not (0 < jx <= r and 0 < jy <= c):
            answer = move
            break
        else:
            for i in range(4):
                njx, njy = dx[i]+jx, dy[i]+jy
                if matrix[njx][njy] == '.' and (njx, njy) not in temp:
                    jin_q.append((njx, njy, move+1))
                    matrix[njx][njy] = 'J'
    else:
        answer = 'IMPOSSIBLE'
        break
        
print(answer)