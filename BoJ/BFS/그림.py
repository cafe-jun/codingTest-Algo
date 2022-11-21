from collections import deque

# f = open('Boj/test.txt')
# n,m = map(int,f.readline().split())
n,m = map(int,input().split())
matrix = []
total_q = deque()
# matrix 만들기 및 1의 좌표를 가진 total_q 만들기 
for i in range(n):
    # tmp = list(map(int,f.readline().split()))
    tmp = list(map(int,input().split()))
    matrix.append(tmp)
    for idx,j in enumerate(tmp):
        # 1인 좌표 확인해서 total_q 에 넣기 
        if j == 1:
            total_q.append((i,idx))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
# 그림 죄표 리스트 
board = []
bfs_q = deque()
# 1인 좌표 돌기 
while total_q:
    mx,my= total_q.popleft()
    # 한번 방문한 좌표
    if matrix[mx][my] != 1:
        continue
    # 한번 방문한 좌표는 0으로 만들기 
    matrix[mx][my] = 0
    # 0이 아니라면 새로운 그림이라고 판단하고 board 에 넣기 
    board.append([(mx,my)])
    # bfs_q에 넣기 
    bfs_q.append((mx,my))
    # bfs 실행 
    while bfs_q:
        x,y = bfs_q.popleft()
        for r in range(4):
            nx = dx[r] + x
            ny = dy[r] + y
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    bfs_q.append((nx,ny))
                    board[-1].append((nx,ny))
                    matrix[nx][ny] = 0
print(len(board))
max_cnt = 0
for b in board:
    max_cnt = max(len(b),max_cnt) 
print(max_cnt)
