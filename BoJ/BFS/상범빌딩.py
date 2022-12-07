
from collections import deque
import sys
input = sys.stdin.readline

# f = open('BoJ/test.txt')

df = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,-1,1]

matrix = []
L,R,C = 0,0,0

def bfs(start,end):
    q = deque()
    q.append(start)
    while q:
        f,x,y,cnt = q.popleft()
        if (f,x,y) == end:
            return 'Escaped in '+str(cnt)+' minute(s).'
        for i in range(6):
            nf,nx,ny = df[i]+f,dx[i]+x,dy[i]+y
            if 0<= nf < L and 0<= nx <R and 0<=ny<C:
                if matrix[nf][nx][ny] != '#':
                    q.append((nf, nx, ny,cnt+1))
                    matrix[nf][nx][ny] = '#'

    else:
        return 'Trapped!'
    


while True:
    # L,R,C = map(int,f.readline().split())
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    start = ''
    end = ''
    matrix = []
    for l in range(L):
        matrix.append([])
        for r in range(R):
            # temp = list(f.readline().strip())
            temp = list(input().strip())
            matrix[-1].append(temp)
            for c,t in enumerate(temp):
                if t == 'S':
                    start = (l,r,c,0)
                    matrix[l][r][c] = '#'
                elif t == 'E':
                    end = (l,r,c) 
        else:
            # f.readline()
            input()
    print(bfs(start,end))
    