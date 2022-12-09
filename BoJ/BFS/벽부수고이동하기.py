

from collections import deque
import sys
input = sys.stdin.readline

f = open('BoJ/test.txt')

N,M = map(int,f.readline().split())
# N,M = map(int,input().split())
matrix = [list(map(int,f.readline().strip())) for _ in range(N)]
# matrix = [list(map(int,input().strip())) for _ in range(N)]
       
          
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(matrix: list[int],break_cnt):
    q = deque()
    q.append((0,0,break_cnt))
    matrix[0][0] = 2
    while q:
        x,y,br = q.popleft()
        if x == N-1 and y == M-1:
            return matrix[x][y]-1
    
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<= nx <N and 0 <= ny <M:
                if matrix[nx][ny] == 0:
                    q.append((nx,ny,br))
                    matrix[nx][ny] = matrix[x][y]+1
                elif matrix[nx][ny] == 1 and br == 0:
                    q.append((nx,ny,1))
                    matrix[nx][ny] = matrix[x][y]+1
    else:
        return -1                         
        
answer = []
wrong_cnt = 0

for i in range(2):
    result =bfs(matrix,i)
    if result == -1:
        wrong_cnt += 1
    else:
        answer.append(result)
else:
    if wrong_cnt == 2:
        print(-1)
    else:
        print(min(answer))    