
from collections import deque


# f = open('BoJ/test.txt')
# n,m = map(int,f.readline().split())
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    arr = map(str,input())
    matrix.append([])
    for i in arr:
        if i == '0' or i == '1':
            matrix[-1].append(i)
    
q = deque()
q.append((0,0,1))
temp = []
temp.append((0,0))
cnt = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while q:
    x,y,cnt= q.popleft()
    if (m,n) == (x+1,y+1):
        print(cnt)
        break;
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0 <= nx < m and 0 <= ny < n and (ny,nx) not in temp:
           if matrix[ny][nx] == '1':
               q.append((nx,ny,cnt+1))
               temp.append((ny,nx)) 
