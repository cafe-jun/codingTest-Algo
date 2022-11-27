from collections import deque
import sys
input = sys.stdin.readline

f = open("BoJ/test.txt")

n = int(f.readline())
matrix = [list(f.readline().strip()) for _ in range(n)]

# n = int(input())
# matrix = [list(input().strip()) for _ in range(n)]
visited = []
ranges = []
b_visited = []
b_ranges = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    for j in range(n):
        if (i,j) not in visited:
           ranges.append([])
           stack = deque()
           stack.append((i,j,matrix[i][j]))
           ranges[-1].append((i,j,matrix[i][j]))
           visited.append((i,j))
           while stack:
               x,y,color = stack.pop()
               for k in range(4):
                   nx,ny=dx[k]+x,dy[k]+y
                   if 0<= nx< n and 0<= ny< n:
                        if color == 'B':
                            if matrix[nx][ny] == color and (nx,ny) not in visited:
                                visited.append((nx,ny))
                                stack.append((nx,ny,matrix[nx][ny]))
                                ranges[-1].append((nx,ny,matrix[nx][ny]))
                        else:
                            if matrix[nx][ny] in ['R','G'] and (nx,ny) not in visited:
                                visited.append((nx,ny))
                                stack.append((nx,ny,matrix[nx][ny]))
                                ranges[-1].append((nx,ny,matrix[nx][ny]))
                                
        if (i,j) not in b_visited:
            b_ranges.append([])
            b_stack = deque()
            b_stack.append((i,j,matrix[i][j]))
            b_ranges[-1].append((i,j,matrix[i][j]))
            b_visited.append((i,j))
            while b_stack:
                bx,by,color = b_stack.pop()
                for k in range(4):
                    nbx,nby=dx[k]+bx,dy[k]+by
                    if 0<= nbx< n and 0<= nby< n:
                        if matrix[nbx][nby] == color and (nbx,nby) not in b_visited:
                            b_visited.append((nbx,nby))
                            b_stack.append((nbx,nby,matrix[nbx][nby]))
                            b_ranges[-1].append((nbx,nby,matrix[nbx][nby]))
                            

print(len(b_ranges),len(ranges),sep=' ')