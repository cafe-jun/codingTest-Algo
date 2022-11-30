
from collections import deque
import sys
input = sys.stdin.readline

# f = open('Boj/test.txt')
# T = int(f.readline())
T = int(input())
answer = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
  
def bfs(f_queue,j_queue,f_visited,j_visited):
    while f_queue:    # fire BFS
            x, y = f_queue.popleft()
    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
    
                if 0 <= nx < H and 0 <= ny < W:
                    if not f_visited[nx][ny] and graph[nx][ny] != '#' and graph[nx][ny] != '*':
                        f_visited[nx][ny] = f_visited[x][y] + 1
                        f_queue.append((nx, ny))
    
    while j_queue:    # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < H and 0 <= ny < W:
                if not j_visited[nx][ny] and graph[nx][ny] != '#'  and graph[nx][ny] != '*':
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:    # important code
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else:
                return j_visited[x][y] + 1    # escape map
    
    return 'IMPOSSIBLE'  


for _ in range(T):
    # W,H = map(int,f.readline().split())
    W,H = map(int,input().split())
    f_visited, j_visited = [[0] * W for _ in range(H)], [[0] * W for _ in range(H)]
    # graph = [list(f.readline().strip()) for _ in range(H)]
    graph = [list(input().strip()) for _ in range(H)]
    f_queue, j_queue = deque(),deque()
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '*':
                f_queue.append((i,j))
            elif graph[i][j] == '@':
                j_queue.append((i,j))
    answer.append(bfs(f_queue,j_queue,f_visited,j_visited))
    
for a in answer:
    print(a)