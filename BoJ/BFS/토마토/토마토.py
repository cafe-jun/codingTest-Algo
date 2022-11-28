
from collections import deque

# f = open('BoJ/test.txt')
# m,n = map(int,f.readline().split())
m,n = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
s = set()
zero_cnt = 0
box = []
for i in range(n):
    arr = list(map(int,input().split()))
    # arr = list(map(int,f.readline().split()))
    box.append(arr)
    for idx,j in enumerate(arr):
        if j == 1:
            q.append((i,idx,0)) 
        elif j == 0:
            zero_cnt +=1
            
            
if zero_cnt == 0:
    print(0)
else:
    while q:
        x,y,day = q.popleft()
        
        for i in range(4):
            nx,ny= dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    q.append((nx,ny,day+1))
                    s.add((nx,ny))
                    box[nx][ny] = 1
                    
    else:
        if zero_cnt != len(s):
            print(-1)
        else:
            print(day)
