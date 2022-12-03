
from collections import deque
import sys
input = sys.stdin.readline
 


# f = open('BoJ/test.txt')
# N = int(f.readline())
N = int(input())
# graph = [list(map(int,f.readline().strip())) for _ in range(N)]
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[True] * N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(point):
    result = 1
    q = deque()
    q.append(point)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 1 and visited[nx][ny] == True:
                    q.append((nx,ny))
                    visited[nx][ny] = False
                    result += 1
    else:
        return result


answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == True:
            visited[i][j] = False
            answer.append(bfs((i,j)));

print(len(answer))
for a in sorted(answer):
    print(a)