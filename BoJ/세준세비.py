f = open('test.txt')

T = int(f.readline())
N = []
M = []
for tc in range(T):
    
    N.append(list(map(int,f.readline())))
    M.append(list(map(int,f.readline())))


f.close()