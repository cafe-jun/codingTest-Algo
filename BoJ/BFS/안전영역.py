from collections import deque
# import sys
# input = sys.stdin.readline

f = open('BoJ/test.txt')

N = int(f.readline())
region = []
max_height = 0
for _ in range(N):
    temp = list(map(int,f.readline().split()))
    region.append(temp)
    for tmp in temp:
        max_height = max(tmp,max_height)
        
                    
visited = [[True] * N for _ in range(N)]
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(q :deque,t:int):
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = dx[k]+x,dy[k]+y
            if 0<= nx <N and 0 <= ny <N:
                if visited[nx][ny] and region[nx][ny] <= t:
                    q.append((i,j))
                    visited[i][j] = False          
            
     
 
for t in range(1,100):
    for i in range(N):
        for j in range(N):
            if visited[i][j] and region[i][j] <= t:
                q.append((i,j))
                visited[i][j] = False     
                bfs(q,t)

            
    