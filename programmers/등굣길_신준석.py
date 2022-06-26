
# 1. 외벽 만들기 
# 2. BFS
# 3, DFS



# def bfs():
#     q = deque()
#     q.append([1,1])
#     while q:
#         y,x = q.popleft()
#         if x == m and y == n:
#             loads[n][m] += 1
#         else: 
#             for i in range(2):
#                 nx = dx[i] +x 
#                 ny = dy[i] +y
#                 if loads[ny][nx] == 1:
#                     if [ny,nx] in vistied:
#                         loads[ny][nx] += 1
#                     else:
#                         vistied.append([ny,nx])
#                     q.append([ny,nx])        

def solution(m: int, n:int, puddles):
    loads = [[-1 for _ in range(m+2)] for _ in range(n+2)] 
    # for i in range(n):
    #     for j in range(m):
    #         if [j+1,i+1] in puddles:
    #             loads[i+1][j+1] = -2
    #         else:
    #             loads[i+1][j+1] = 0
    def dfs(x,y) :
        if not (1 <= x <= n and 1 <= y <= m):
            return 0    
        if [y,x] in puddles:
            return 0
        if [x,y] == [n,m]:
            return 1
        if loads[x][y] != -1:
            return loads[x][y]
        dy = [0,1]
        dx = [1,0]
        for i in range(2):
            nx = dx[i] +x 
            ny = dy[i] +y    
            loads[x][y] += dfs(nx,ny)
        return loads[x][y]
    answer =dfs(1,1)
    print('')
    return answer %  (10 ** 9 + 7)
    

print(solution(4,3,[[2,2]]))


dx = [0, 1]
dy = [1, 0]


def solution(m, n, puddles):
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m):
            return 0
        if [y + 1, x + 1] in puddles:
            return 0
        if [x, y] == [n - 1, m - 1]:
            return 1

        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 0
        for i in range(2):
            dp[x][y] += dfs(x + dx[i], y + dy[i]) % (10 ** 9 + 7)

        return dp[x][y]

    answer = dfs(0, 0)
    return answer % (10 ** 9 + 7)