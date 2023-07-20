from collections import deque


def solution(board: list[str]):
    answer = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque()
    goal = []
    visied = []
    for idx,b in enumerate(board):
        for jdx,a in enumerate(b):
            if board[idx][jdx] == 'R':
                q.append((idx,jdx,0))
                visied.append((idx,jdx))
                break
        else:
            break;

    
    while q:
        x,y,cnt = q.popleft()
        if board[x][y] == 'G':
            answer = cnt
            break;
        
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            # 슬라이딩 
            sliding = False
            while 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] != 'D' and board[nx][ny] != 'G' and (nx,ny) not in visied:
                temp_x = nx
                temp_y = ny
                
                ny += dy[i]    
                nx += dx[i]
                sliding = True
            else:
                if sliding == True:
                    q.append((temp_x,temp_y,cnt+1))
                    visied.append((temp_x,temp_y))
            
    return answer



print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))