
# from collections import deque
# visited = [[False] * n for _ in range(n)]
# move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# graph = [[] * n for _ in range(n)]

# for i in range(n):
# 	color = str(input())
#     for x in color:
#     	graph[i].append(x)

# def bfs(x, y, color):
# 	q = deque()
#     q.append([x, y])
    
#     while q:
#     	loc = q.popleft()
#         x = loc[0]
#         y = loc[1]
        
#         if visited[x][y] == False:
#         	visited[x][y] = True
#         	for i in range(4):
#         		nx, ny = x + move[i][0], y + move[i][1]
#         		if nx >= 0 and nx < n and ny >= 0 and ny < n:
# 	                if graph[nx][ny] == color:
#                     	q.append([nx, ny])

# cnt = 0
# for i in range(n):
# 	for j in range(n):
#     	if visited[i][j] == False:
#         	color = graph[i][j]
#             bfs(i, j, color)
#             cnt += 1

# # 색약일 때
# visited = [[False] * n for _ in range(n)]
# for i in range(n):
# 	for j in range(n):
#     	if graph[i][j] == 'G':
#         	graph[i][j] = 'R'

# cnt_color_weakness = 0
# for i in range(n):
# 	for j in range(n):
#     	if visited[i][j] == False:
#         	color = graph[i][j]
#             bfs(i, j, color)
#             cnt_color_weakness += 1