from collections import deque
import sys

input = sys.stdin.readline
# f = open('Boj/test.txt')
# T = int(f.readline())
T = int(input())

dx = [2,2,1,1,-2,-2,-1,-1]
dy = [-1,1,2,-2,1,-1,2,-2]
# T = int(input())
answer = []
for _ in range(T):
    # I = int(f.readline())
    I = int(input())
    matrix = [[0 for _ in range(I)] for _ in range(I)]
    # i,j = map(int,f.readline().split())
    i,j = map(int,input().split())
    matrix[i][j] = 1
    q = deque()
    q.append((i,j,0))
    end = list(map(int,input().split()))
    # end = list(map(int,f.readline().split()))
    while q:
        x,y,cnt = q.popleft()
        if end[0] == x and end[1] == y:
            answer.append(cnt)
            break
        
        for i in range(8):
            nx,ny= dx[i]+x,dy[i]+y
            if 0<= nx <I and 0<= ny <I:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny]=1
                    q.append((nx,ny,cnt+1))         
                    
for a in answer:
    print(a)