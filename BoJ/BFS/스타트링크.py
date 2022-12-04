from collections import deque
import sys
input = sys.stdin.readline

# f = open('BoJ/test.txt')
# F, S, G, U, D = map(int,f.readline().split())
F, S, G, U, D = map(int,input().split())
visited = [True for _ in range(F+1)]

def bfs():
    q = deque()
    q.append((S,0))
    visited[S] = False
    while q:
        x,cnt = q.popleft()
        if x == G:
            return cnt        
        for i in (x+U,x-D):
            if  1<= i <= F:
                if visited[i]:
                    q.append((i,cnt+1))
                    visited[i] = False
    else:
        return 'use the stairs'

print(bfs())