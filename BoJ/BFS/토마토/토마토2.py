
from collections import deque
# import sys
# input = sys.stdin.readline
f = open('BoJ/test.txt')
M,N,H=map(int,f.readline().split(' '))
# M,N,H=map(int,input().split(' '))

boxs = [] 
q = deque()
for i in range(H):
    boxs.append([])
    for j in range(N):
        temp = list(map(int,f.readline().split()))
        # temp = list(map(int,input().split()))
        boxs[-1].append(temp)
        for idx,k in enumerate(temp):
            if k == 1:
                q.append((i,j,idx,0))
                

dx = [1,-1,0,0]
dy = [0,0,-1,1]
answer = 0
while q:
    h,n,m,day = q.popleft()
    # 앞 
    if 0<=h+1<H:
        if boxs[h+1][n][m] == 0: 
            boxs[h+1][n][m] = boxs[h][n][m]+1
            q.append((h+1,n,m,day+1))
            
    # 뒤
    if 0<=h-1<H:
        if boxs[h-1][n][m]  == 0: 
            boxs[h-1][n][m] = boxs[h][n][m]+1
            q.append((h-1,n,m,day+1))
            
    for i in range(4):
        nx,ny= dx[i]+n,dy[i]+m
        if 0<=nx<N and 0<=ny<M:
            if boxs[h][nx][ny] == 0:
                boxs[h][nx][ny] = boxs[h][n][m]+1
                q.append((h,nx,ny,day+1))
else:
    for a in range(H):
        for b in range(N):
            for c in range(M):
                if boxs[a][b][c] == 0:
                    print(-1)
                    exit(0)
    else:
        print(day)