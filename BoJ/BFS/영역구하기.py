
from collections import deque
import sys
input = sys.stdin.readline
 

f = open('BoJ/test.txt')

M,N,K = map(int,f.readline().split())
# M,N,K = map(int,input().split())
matrix = [[0 for _ in range(N)] for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
  
def bfs(q:deque):
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[nx][ny] == 0:
                    q.append((nx,ny))
                    matrix[nx][ny] = 1
                    cnt +=1
    return cnt
    
    
for _ in range(K):
    start_y,start_x,end_y,end_x =map(int,f.readline().split())
    # start_y,start_x,end_y,end_x =map(int,input().split())
    for i in range(abs(end_x-start_x)):
        for j in range(abs(end_y-start_y)):
            matrix[start_x+i][start_y+j] = 1
        
answer = []
q = deque()
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            q.append((i,j))
            answer.append(bfs(q))
else:
    print(len(answer))
    for idx,a in enumerate(sorted(answer)):
        if idx < len(answer)-1:
            print(a,end=" ")
        else:
            print(a)