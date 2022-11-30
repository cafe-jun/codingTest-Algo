
f = open('Boj/test.txt')
T = int(f.readline())

def bfs():
    pass


for _ in range(T):
    W,H = map(int,f.readline().split())
    
    f_visited, j_visited = [[0] * H for _ in range(W)], [[0] * H for _ in range(W)]

