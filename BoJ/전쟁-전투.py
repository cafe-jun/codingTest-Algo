from collections import deque


f = open('Boj/test.txt')
N,M = list(map(int,f.readline().split()))
# N,M = list(map(int,input().split()))
matrix = []
for i in range(M):
    ss = map(str,f.readline().split())
    # ss = map(str,input().split())
    for i,s in enumerate(ss):
        matrix.append([])
        for j,c in enumerate(s):
            matrix[-1].append(c)


# f.close()
def solution(matrix: list[str]):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    lset = {'B' : [],'W': []}
    # bfs 구현하기 
    q = deque()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 'X':
                continue
            else:
                m = matrix[i][j]
                matrix[i][j] = 'X'
                lset[m].append(set())
                lset[m][-1].add((i,j))
                q.append((i,j))
                while q:
                    (x,y) = q.popleft()
                    for t in range(4):
                        nx = dx[t] + x
                        ny = dy[t] + y
                        if 0 <= nx< M and 0 <= ny < N:
                            if matrix[nx][ny] == m and matrix[nx][ny] != 'X':
                                matrix[nx][ny] = 'X'
                                q.append((nx,ny))
                                lset[m][-1].add((nx,ny))
    w_total = 0
    b_total = 0 
    for key in lset.keys():
        for c in lset[key]:
            if key == 'W':
                w_total += len(c)*len(c)
            else:
                b_total += len(c)*len(c)
    return str(w_total)+' '+str(b_total)

        
    
    
    

print(solution(matrix))
