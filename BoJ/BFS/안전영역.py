from collections import deque
from copy import deepcopy
# import sys
# input = sys.stdin.readline

# f = open('BoJ/test.txt')
# N = int(f.readline())
N = int(input())
region = []
max_height = 0
for _ in range(N):
    # temp = list(map(int,f.readline().split()))
    temp = list(map(int,input().split()))
    region.append(temp)
    for tmp in temp:
        max_height = max(tmp,max_height)
        
visited = [[True] * N for _ in range(N)]
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(q :deque,t:int,c_visited):
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = dx[k]+x,dy[k]+y
            if 0<= nx <N and 0 <= ny <N:
                if c_visited[nx][ny] and region[nx][ny] > t:
                    q.append((nx,ny))
                    c_visited[nx][ny] = False          
            
     
answer = 0
for t in range(max_height,0,-1):
    c_visited = deepcopy(visited)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if c_visited[i][j] and region[i][j] > t:
                q.append((i,j))
                c_visited[i][j] = False
                bfs(q,t,c_visited)
                cnt += 1
    else:
        answer = max(answer,cnt)
        

print(answer)
