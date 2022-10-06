from collections import deque

direction = { 'left': [1,0],'down': [0,1],'right': [-1,0],'up': [0,-1]}

def solution(board: list[int]):
    global matrix_b,n,bbs,vistied
    vistied = []
    bbs = board
    answer = 0
    n = len(bbs)
    matrix_b = [[500*(n*n) for _ in range(n)] for _ in range(n)]
    matrix_b[0][0] = 100
    # dfs 로 하면 너무 많은 depth 가 생겨 안됨 => 제가 조건을 잘 안한걸수도 있음 (visited을 빼서)
    q = deque()
    vistied = []
    q.append((0,0,'down'))
    q.append((0,0,'left'))
    
    vistied.append((0,0,'left'))
    vistied.append((0,0,'down'))
    
    while q:
        x, y, d = q.popleft()
        for direct in direction.keys():
            #print(direction[direct])
            nx = direction[direct][0] + x
            ny = direction[direct][1] + y
            if 0 <= nx < n and 0 <= ny < n and (ny,nx,direct) not in vistied:
                bill = 0
                if matrix_b[ny][nx] != 1:
                    if d in ["left",'right'] and direct in ["left",'right']:
                        bill = matrix_b[y][x] + 100
                    elif d in ["up",'down'] and direct in ["up",'down']:
                        bill = matrix_b[y][x] + 100
                    else:
                        bill = matrix_b[y][x] + 500
                    matrix_b[ny][nx] = min(matrix_b[ny][nx],bill)
                    vistied.append((ny,nx,direct))
                    q.append((ny,nx,direct))
                    
    print(matrix_b)
    vistied.clear()
    return answer[0]

# def dfs(y,x,d):
#     if (n-1,n-1) == (y,x):
#         matrix_b[n-1][n-1] = 100
#         print('시작')
#         return [matrix_b[n-1][n-1],d]
#     # 코너 빠짐 로직 
#     for direct in direction.keys():
#         # 현재 이동방향과 같을경우 
#         nx = direction[direct][0] + x
#         ny = direction[direct][1] + y
#         # 현재 이동방향과 다르게 갈경우 
#         #print('시도 ',direct,(ny,nx))
#         if 0 <= nx < n and 0<=ny<n and (ny,nx,direct):
#             #print('성공 ',direct,(ny,nx))
#             if bbs[ny][nx] != 1:
#                 bill,next_d = dfs(ny,nx,direct)
#                 if next_d != d:
#                     bill += 500
#                 else:
#                     bill += 100
#                 matrix_b[y][x] = min(matrix_b[y][x],bill)
#         #else:
#             #print('실패 ',direct,(ny,nx))
#     return [matrix_b[y][x],d]
        
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 900)
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
      0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]) == 3800)
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 2100)
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]) == 3200)


    
    
    # while q:
    #     x, y, d = q.popleft()
    #     for i in range(4):
    #         nx = dx[i] + x
    #         ny = dy[i] + y
    #         if 0 <= nx < n and 0 <= ny < n:
    #             temp_b = matrix_b[x][y]
    #             temp_d = d
    #             if d == 'h' and i in [0, 1]:
    #                 temp_b += 400
    #                 temp_d = 'v'
    #             elif d == 'v' and i in [2, 3]:
    #                 temp_b += 400
    #                 temp_d == 'h'
    #             else:
    #                 temp_b += 100
    #             if (nx, ny, temp_d) not in visted:
    #                 matrix_b[nx][ny] = min(temp_b, matrix_b[nx][ny])
    #                 q.append((nx, ny, temp_d))
    #                 visted.append((nx, ny, temp_d))
    # print(matrix_b)