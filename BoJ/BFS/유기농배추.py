from collections import deque
import sys
input = sys.stdin.readline
 

# f = open("BoJ/test.txt")
T = int(input())
# T = int(f.readline())
# M 가로 길이 N 은 세로길이 K 배추 좌표 
graphs = []
di = [1,-1,0,0]
dj = [0,0,1,-1]
answer = []
for _ in range(T):
    M,N,K = map(int,input().split())
    # M,N,K = map(int,f.readline().split())
    graphs = [[0 for _ in range(N)] for _ in range(M)]
    point = []
    for _ in range(K):
        x,y = map(int,input().split())
        # x,y = map(int,f.readline().split())
        point.append((x,y))
        graphs[x][y] = 1
    cnt = 0
    visited = []    
    for p in point:
        dq = deque()
        if p in visited:
            continue
        else:
            visited.append(p)
            dq.append(p)
            while dq:
                i,j = dq.pop()
                for k in range(4):
                    ni = di[k]+i
                    nj = dj[k]+j
                    if 0<= ni < M and 0<= nj < N:
                        if graphs[ni][nj] == 1 and (ni,nj) not in visited:
                            dq.append((ni,nj))
                            visited.append((ni,nj))                        
            else:
                cnt += 1
    else:
        answer.append(cnt)

else:
    for a in answer:
        print(a)
        
