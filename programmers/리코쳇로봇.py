from collections import deque


def solution(board: list[str]):
    answer = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    n = len(board)
    m = len(board[0])
    
    
    q = deque()
    matrix = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    for idx in range(len(board)):
        for jdx in range(len(board[0])):
            if board[idx][jdx] == 'R':
                q.append((idx,jdx))
                matrix[idx][jdx] = 1

    
    while q:
        x,y = q.popleft()
        if board[x][y] == 'G':
            return matrix[x][y]-1
            
        
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y]+1
                q.append((nx,ny))
    return -1



print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))