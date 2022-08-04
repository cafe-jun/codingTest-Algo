

from copy import deepcopy


dir = ((-1,0),(0,1),(1,0),(0,-1))

def A_turn(ar,ac,br,bc,cnt,board):
    if board[ar][ac] == 0:
        return (1,cnt)
    winner = []
    loser = []
    flag = False
    for dr,dc in dir:
        nr,nc = ar+dr,ac+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [row[:] for row in board]
            temp[ar][ac] = 0
            iswin,turn = B_turn(br,bc,nr,nc,cnt+1,temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def B_turn(br,bc,ar,ac,cnt,board):
    if board[br][bc] == 0:
        return (1,cnt)
    winner = []
    loser = []
    flag = False
    for dr,dc in dir:
        nr,nc = br+dr,bc+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [row[:] for row in board]
            temp[br][bc] = 0
            iswin,turn = A_turn(ar,ac,nr,nc,cnt+1,temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def solution(board, aloc, bloc):
    ar,ac,br,bc = aloc[0],aloc[1],bloc[0],bloc[1]
    answer = A_turn(ar,ac,br,bc,0,board)[1]
    return answer

# dfs 로 푼 풀이 
# def solution(board, aloc, bloc):
#     answer = 0

#     deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

#     def neighbor(loc, board):
#         for dx, dy in deltas:
#             n = (loc[0]+dx, loc[1]+dy)
#             if n in board:
#                 yield (*n, loc[2])

#     def dfs(aloc, bloc, board, depth):
#         neighbors = list(neighbor(aloc, board))

#         if not neighbors or aloc[:2] not in board:
#             return 0, depth

#         res = list(dfs(bloc, n, board - {aloc[:2]}, depth + 1) for n in neighbors)
#         wins = [r[1] for r in res if r[0] == 0]
#         loses = [r[1] for r in res if r[0] == 1]

#         if wins:
#             return 1, min(wins)
#         else:
#             return 0, max(loses)


#     board = {(r, c) for r, row in enumerate(board) for c, val in enumerate(row) if val}
#     answer = dfs(tuple(aloc + [0]), tuple(bloc + [1]), board, 0)[1]

#     return answer

# def solution(board, aloc, bloc):
#     answer = -1
#     tmp_set = set()
#     visited = []
#     ax,ay = aloc
#     bx,by = bloc
#     stack = []
#     stack.append((ax,ay,bx,by,'A',0,0,[]))
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     log_list = []
#     while stack:
#         ax,ay,bx,by,turn,amove,bmove,visited = stack.pop()
        
#         if (ax,ay) == (bx,by):
#             if turn == 'A':
#                 tmp_set.add((amove+1,bmove,'A'))
#             else:
#                 tmp_set.add((amove,bmove+1,'B'))
#             continue
#         # 통과 가능성 
#         for i in range(4):
#             cnt = 0
#             tmp_visited = deepcopy(visited)
#             if turn == 'A':
#                 nx = ax+dx[i]
#                 ny = ay+dy[i]
#             else:
#                 nx = bx+dx[i]
#                 ny = by+dy[i]
                
            
#             if 0<=nx<=len(board)-1 and 0<=ny<=len(board[0])-1:
#                 if board[nx][ny] == 1 and (nx,ny) not in tmp_visited:
#                     if turn == 'A':
#                         tmp_visited.append((ax,ay)) 
#                         stack.append((nx,ny,bx,by,'B',amove+1,bmove,tmp_visited))
#                     else:
#                         tmp_visited.append((bx,by)) 
#                         stack.append((ax,ay,nx,ny,'A',amove,bmove+1,tmp_visited))
#                     cnt += 1
#                     # 갈대가 없다 
#             if cnt == 0:
#                 if turn == 'A':
#                     tmp_set.add((amove,bmove,'B'))
#                 else:
#                     tmp_set.add((amove,bmove,'A'))

#     print(log_list)
#     print(answer)
#     return answer




print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1, 0],[1, 2]) == 5)
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]],[1, 0],[1, 2]) == 4)
print(solution([[1, 1, 1, 1, 1]],[0, 0],[0, 4]) == 4)
print(solution([[1]],[0, 0],[0, 0]) == 0)