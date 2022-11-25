from copy import deepcopy


f = open("BoJ/test.txt")
# T = int(input())
T = int(f.readline())
# M 가로 길이 N 은 세로길이 K 배추 좌표 
# M,N,K = map(int,input().split())
# M,N,K = map(int,f.readline().split())
graph_case = []
point_cases = []
for _ in range(T):
    M,N,K = map(int,f.readline().split())
    point_cases.append([])
    graph_case.append((M,N))
    for _ in range(K):
        point_cases[-1].append(tuple(map(int,f.readline().split())))
    


# copy_g = deepcopy(graph)
# graph = [[0 for _ in range(N)] for _ in range(M)]